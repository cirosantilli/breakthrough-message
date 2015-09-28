"""
Common functions.
"""

import subprocess
import os

from order import order

txt_zero = ' '
txt_one = 'X'
txt_sep = '---\n'
payload_dir = 'payloads'
image_dir = 'images'
intermediate_suffix = '_.png'
output_suffix = '_.gray'

nprimes = 100000

# The first nprimes primes.
# Used for the beacon and image dimensions.
# It is a bit ugly to hardcode it, but there is no precise formula to quantify this,
# and we'd have to go to too much trouble to determine the widths we need...
# So we just take 100k which is instantaneous to calculate and should be enough.
primes = []
numbers = set(range(nprimes, 1, -1))
while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p * 2, nprimes + 1, p)))

payload_id_properties = {}
for payload_basename in os.listdir(payload_dir):
    payload_path = os.path.join(payload_dir, payload_basename)
    if os.path.isfile(payload_path):
        payload_id, ext = os.path.splitext(payload_basename)
        payload_id_properties[payload_id] = {'path': payload_path, 'type': ext[1:]}

image_id_path = {}
for image_basename in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_basename)
    if os.path.isfile(image_path):
        image_id, ext = os.path.splitext(image_basename)
        image_id_path[image_id] = image_path

def txt_process_image(image_string):
    lines = image_string.splitlines()
    max_len = max([len(line) for  line in lines])
    output = []
    for line in lines:
        output_line = []
        for c in line:
            if c == txt_zero:
                pixel = False
            elif c == txt_one:
                pixel = True
            else:
                raise Exception('Invalid image byte: ' + c)
            output_line.append(pixel)
        output_line.extend([False] * (max_len - len(line)))
        output.append(output_line)
    return output

def txt_split(payload_encoded):
    parts = payload_encoded.split(txt_sep)
    if len(parts) == 2:
        comment = ''
        start_index = 0
    elif len(parts) == 3:
        comment = parts[0]
        start_index = 1
    else:
        raise Exception('Invalid number of separators: ' + txt_sep)
    text = parts[start_index]
    if text[-1] == '\n':
        text = text[:-1]
    image = parts[start_index + 1]
    return comment, text, image

def txt_process(payload_encoded):
    comment, text, image = txt_split(payload_encoded)
    image = txt_process_image(image)
    return comment, text, image

def img_process_image(image_id, payload_encoded):
    image_path = image_id_path[image_id]
    image_path_noext = os.path.splitext(image_path)[0]
    # Add `_` to avoid conflict with the image id.
    # This path exists to:
    # - add the image to the html view
    # - make it easier to inspect while developing
    intermediate_path = image_path_noext + intermediate_suffix
    output_path =  image_path_noext + output_suffix
    width = int(payload_encoded)
    if (not os.path.exists(output_path)
            or os.path.getmtime(output_path) < os.path.getmtime(image_path)):

        command = [
            'convert',
            image_path,
            '-depth',
            '8',
            '-resize',
            str(width),
            '-monochrome',
            intermediate_path
        ]
        process = subprocess.Popen(
            command,
            shell  = False,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines = True
        )
        exit_status = process.wait()
        assert exit_status == 0

        command = [
            'convert',
            intermediate_path,
            output_path
        ]
        process = subprocess.Popen(
            command,
            shell  = False,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines = True
        )
        exit_status = process.wait()
        assert exit_status == 0

    output = []
    with open(output_path, 'r') as f:
        while True:
            line = f.read(width)
            if line == '':
                break
            output_line = []
            for c in line:
                if c == '\x00':
                    pixel = True
                else:
                    pixel = False
                output_line.append(pixel)
            output.append(output_line)
    return output

def img_process(payload_id, payload_encoded):
    comment, text, image = txt_split(payload_encoded)
    image = img_process_image(payload_id, image)
    return comment, text, image

def payload_iterator():
    for payload_id in order:
        payload_property = payload_id_properties[payload_id]
        with open(payload_property['path'], 'r') as f:
            payload_encoded = f.read()
        payload_type = payload_property['type']
        if payload_type == 'txt':
            comment, text, image = txt_process(payload_encoded)
        elif payload_type == 'img':
            comment, text, image = img_process(payload_id, payload_encoded)
        else:
            raise Exception('Unknown payload type: ' + payload_type)
        yield({'id': payload_id, 'comment': comment, 'text': text, 'image': image})
