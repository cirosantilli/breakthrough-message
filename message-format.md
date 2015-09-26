# Message format

## Packet

The message will be made up of multiple packets concatenated directly.

A packet is composed of:

- Beacon
- Packet ID
- Beacon
- Payload size
- Beacon
- Payload

## Beacon

Beacon: encode the first N primes in base-1 as proposed by Carl Sagan in Cosmos, e.g.:

    B = 1 0 1 1 0 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 1 0 ...
        ^   ^^^   ^^^^^   ^^^^^^^^^   ^^^^^^^^^^^^^

This is what will capture the attention of aliens. We suppose that no known astronomical process produces such string.

This string will be used as a separator, much like we use spaces as separators. So it will be sent *a lot* of times.

This will reduce our bandwidth a lot, but it does not matter: getting notice is priority one.

This will be sent so often that they will easily deduce it is a separator.

If the length is too bit, we may consider using more than one `0` to separate each prime to account for transmission errors.

## Message ID

Starts on 0, and increases with each message.

Width will be fixed, and the number encoded in binary, e.g.:

    0 0 0 0
    0 0 0 1
    0 0 1 0
    0 0 1 1

We would have to pick a width big enough to send all our messages. 64-bit should be plenty.

It should be easy for aliens to see that this is binary and that the number is increasing.

If sending the entire data takes a considerable amount of time, we can consider a system that sends the first messages more often than later ones, e.g.:

- send the first 1k messages
- send the second 1k messages
- send the first 1k messages
- ...

## Payload size

We could omit this if we are sure that the beacon is not present in any payload, but let's just use it and be saner.

Aliens will easily deduce this.

We can't send payloads that are too long or else the beacon will be sent to rarely, so it will be more likely that they will not notice it.

## Payload

This is the actual data to be sent, while other fields are just metadata.

Its format will not be discussed in this section.

## Error detection

I know nothing about radio telescopes, what is the expected error rate?

If too high, we can just send messages more than once, I don't think it will be easy to explain Huffman coding to them at first :-)
