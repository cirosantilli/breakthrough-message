"""
Common functions.
"""

import os

from order import order

txt_zero = ' '
txt_one = 'X'
txt_sep = '---\n'
payload_dir = 'payloads'
payload_data_path = 'data'

nprimes = 100000

# The first nprimes primes.
# Used for the beacon and image dimensions.
# It is a bit ugly to hardcode it, but there is no precise formula to quantify this,
# and we'd have to go to too much trouble to determine the widths we need...
# So we just take 100k which is instanteneous to calculate and should be enough.
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

def process_image(image_string):
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

def payload_iterator():
    for payload_id in order:
        payload_property = payload_id_properties[payload_id]
        with open(payload_property['path'], 'r') as f:
            payload_encoded = f.read()
        payload_type = payload_property['type']
        if payload_type == 'txt':
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
            image = process_image(parts[start_index + 1])
            yield({'id': payload_id, 'comment': comment, 'text': text, 'image': image})
