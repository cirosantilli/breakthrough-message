#!/usr/bin/env python

"""
Generate a decoded HTML view of the data,
for people to quickly see if the message makes sense.
"""

import os

import breakthrough

demo_dir = 'demo'
clean_width = 50
out_path = os.path.join(demo_dir, 'index.html')

html_head = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Breakthrough Message Demo</title>
<style>
table {
    border-collapse: collapse;
    border: 1px solid black;
    margin-top: 5px;
}
td {
    border: 1px solid black;
    height: 10px;
    width: 10px;
}
td.black {
    background-color: black;
    border: 1px solid white;
}
/*
This table is better to see large photos
or else the borders get in the way.
*/
table.clean td {
    border: 0px;
    height: 1px;
    width: 1px;
}
span {
    border: 1px solid black;
    display: inline-block;
    height: 10px;
    width: 10px;
}
span.black {
    background-color: black;
    border: 1px solid white;
}
img {
    display: block;
    margin-top: 5px;
}
</style>
</head>
<body>
<h1>Breakthrough Message Demo</h1>

<h2>What is this?</h2>
<p>This is a proposal for the <a href="http://breakthroughinitiatives.org/initiative/2">breakthrough message contest</a>.</p>
<p>The source is available at: <a href="https://github.com/cirosantilli/breakthrough-message">https://github.com/cirosantilli/breakthrough-message</a></p>
<p>This is only a human viewable view of this message to help sell and test this proposal.</p>
<p>We are not going to send an HTML to aliens! But the same raw data that we used to generate this file can also be used to generate the actual message in a format that (we hope!) will be easy for the aliens to figure out.</p>
<p>The message is composed of multiple text / image pairs.</p>
<p>Images will be black / white binary 1 bit per pixel to make it simple for the aliens to understand it.</p>
<p>Of course, you have the obvious advantage of knowing English to read the text part of the message.</p>
<p>But we believe that by sending multiple that use the some words multiple times, the aliens will be able to do some string matching and image interpretation, and deduce what some of the words mean.</p>
<p>The main goal of this message is to explain to aliens where we are inside the Milky way so they can find us. TODO: we are not there yet.</p>

<h2>Message</h2>
'''

html_tail = '''</body>
</html>
'''

def write_table(out_file, image, table_class):
    out_file.write('<table class="{}">'.format(table_class))
    for line in image:
        out_file.write('<tr>')
        for pixel in line:
            if pixel:
                klass = 'black'
            else:
                klass = 'white'
            out_file.write('<td class="{}">'.format(klass))
            out_file.write('</td>\n')
        out_file.write('</tr>\n')
    out_file.write('</table>\n')

with open(out_path, 'w') as out_file:
    out_file.write(html_head)
    for payload in breakthrough.payload_iterator():
        out_file.write(payload['text'])
        image = payload['image']
        width = len(image[0])

        # Use images for large pictures.
        # This is the only fast way I've found so far: tables are far too slow.
        # I wonder if SVG would be faster... but lazy to code it.
        if width < clean_width:
            write_table(out_file, image, '')
        else:
            img_basename = payload['id'] + breakthrough.intermediate_suffix
            img_orig = os.path.join(breakthrough.image_dir, img_basename)
            if os.path.exists(img_orig):
                os.rename(img_orig, os.path.join(demo_dir, img_basename))
            out_file.write('<img src="{}">\n'.format(img_basename))

        """
        # HTML table attempt. Big tables are too slow.
        if width > clean_width:
            table_class = 'clean'
        else:
            table_class = ''
        write_table(out_file, image, table_class)
        """

        """
        # span test.
        out_file.write('<br/>')
        for line in image:
            for pixel in line:
                if pixel:
                    klass = 'black'
                else:
                    klass = 'white'
                out_file.write('<span class="{}">'.format(klass))
                out_file.write('</span>')
            out_file.write('<br/>')
        """

        out_file.write('<hr/>\n')
    out_file.write(html_tail)
