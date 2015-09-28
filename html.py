#!/usr/bin/env python

"""
Generate a decoded HTML view of the data,
for people to quickly see if the message makes sense.
"""

import breakthrough

out_path = 'index.html'

html_head = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Breakthrough Message</title>
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
</style>
</head>
<body>
<h1>Breakthrough Message</h1>

<h2>What is this?</h2>
<p>This is a proposal for the <a href="http://breakthroughinitiatives.org/initiative/2">breakthrough message contest</a>.</p>
<p>The source is available at: <a href="https://github.com/cirosantilli/breakthrough-message">https://github.com/cirosantilli/breakthrough-message</a></p>
<p>This is only a human viewable view of this message to help sell and test this proposal.</p>
<p>We are not going to send an HTML to aliens! But the same raw data that we used to generate this file can also be used to generate the actual message in a format that (we hope!) will be easy for the aliens to figure out.</p>
<p>The message is composed of multiple text / image pairs.</p>
<p>Images will be black / white binary 1 bit per pixel to make it simple for the aliens to understand it.</p>
<p>Of course, you have the obvious advantage of knowing English to read the text part of the message.</p>
<p>But we believe that by sending multiple that use the some words multiple times, the aliens will be able to do some string matching and image interpretation, and what some of the words mean.</p>
<p>The main goal of this message is to explain to aliens where we are inside the Milky way so they can find us.</p>

<h2>Message</h2>
'''

html_tail = '''</body>
</html>
'''

with open(out_path, 'w') as out_file:
    out_file.write(html_head)
    for payload in breakthrough.payload_iterator():
        print payload
        out_file.write(payload['text'])
        out_file.write('<table>')
        for line in payload['image']:
            out_file.write('<tr>')
            for pixel in line:
                if pixel:
                    klass = 'black'
                else:
                    klass = 'white'
                out_file.write('<td class="{}">'.format(klass))
                out_file.write('</td>')
            out_file.write('</tr>')
        out_file.write('</table>')
        out_file.write('<hr/>')
    out_file.write(html_tail)
