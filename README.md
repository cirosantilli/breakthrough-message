# Breakthrough message

<http://breakthroughinitiatives.org/Initiative/2>

## Format

The global format is:

    | Beacon | Message ID | Beacon | Image width | Beacon | Image |

### Beacon

Beacon: encode the first N primes in base-1 as proposed by Carl Sagan, e.g.:

    B = 1 0 1 1 0 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 1 0 ...
        ^   ^^^   ^^^^^   ^^^^^^^^^   ^^^^^^^^^^^^^

We abbreviate beacon as `B` in this description.

This is what will capture the attention of aliens. We suppose that no known astronomical process produces such string.

This string will be used as a separator, much like we use spaces as separators. So it will be sent *a lot* of times.

This will reduce our bandwidth a lot, but it does not matter: getting notice is priority one.

This will be sent so often that they will easily deduce it is a separator.

### Message ID

Increases with each message.

Width will be fixed, and the number encoded in binary.

We can expect aliens to understand binary I think, and to see that the number is increasing.

If sending the entire data takes a considerable amount of time, we can consider a system that sends the first messages more often than later ones.

### Image width

We could omit this if we are sure that the beacon is not present in any image, but let's just use it and be saner.

Aliens will easily deduce this.

We can't send images that are too long or else the beacon will be sent to rarely, so it will be more likely that they will not notice it.

### Image

Width and height must be primes so that there is only one interpretation possible.

Maybe we should just send 256-bit gray level images as it is easier to interpret.

The later on, after we explain light frequencies to them, we might consider a color format.

Images are of course the only way to start communication.

## Which images to send

Now comes the hard part.

We should of course start with mathematics, physics and chemistry lessons, which the aliens can certainly understand.

Some important things to send:

- numbers. We can use only binary with them.
- atoms
- molecules like water
- spectrum

In each image, we can draw the physical concept, and at the bottom of the image write the name for the concept in English to teach them language.

Further on, we can start sending images that explain new formats.

For example, once they understand English... we can send a message that explains that the image is now a generic payload which contains metadata that says what the format is. One of those formats would be English.

## TODO

Write a Python script that concatenates a bunch of images into the desired format.
