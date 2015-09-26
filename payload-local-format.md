# Payload local format

How we encode the payloads in this repository under [payloads](payloads/).

## Payload order

Each file contains both the text to be sent, and the image, thus two packets.

The order in which payloads will be sent is stored under [order.py](order.py), which contains a Python array of strings.

Each string corresponds to a file in under `payloads` directory without extension.

For example string:

    count1

can correspond to either:

- `count1.txt`
- `count1.imt`
- etc.

Conclusion: filenames without extension must be unique.

## txt

The simplest format to generate by hand.

Example:

    Optional comment.

    Explains rationale for the image.

    Will not be part of the output.
    ---
    heart
    ---
     XX XX
    X  X  X
     X   X
      X x
       X

Format: consist of the following parts separated by `---\n`:

-   comment (optional)

-   text

    Text that will be sent.

    The last newline is discarded.

-   image

    - a space means `0`, and an `X` means `1`
    - if a line is less wide than the widest line, it gets `0` padded to equal the widest line in width
    - lines an columns get zero padded to the next prime width and height
    - newlines are stripped

## img

Format that uses an external image, meant for photographs.

Example:

    Optional comment.
    ---
    heart
    ---
    500

For each such `XXX.img` file, an image in a common format like `XXX.png` will be put in the same directory.

The format is analogous to `txt`, except that the image field holds the width of the image, with the height scaled proportionally.

The image will then be converted as follows:

- converted to black and white with some dithering algorithm
- width is converted to smallest prime below it
- height is center cropped to the nearest smaller prime

This could be implemented with ImageMagick as:

    convert -resize <prime-width> -monochrome in.jpg out.jpg
