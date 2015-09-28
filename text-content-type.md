# Text format

To help differentiate from the images, we could pad text messages to a prime length 1 x N with an unused character. Then as long as we don't use unidimensional images, this would make them distinct. Of course, it would not be long before the aliens notice the odd / even pattern used, so maybe this is not needed?

## Charcter set

Absolutely necessary characters:

- `a-z`
- `0` and  `1` for all numbers
- space to separate words

This totals 29 characters. So we might use 5 bits per character which can encode 32 characters.

A possible good encoding order would be:

-   0 and 1 first, since they are special character (represent numbers), and in this way would map to their binary representation

-   a-z

-   space last.

    The space has a very special meaning very different from the other characters.

    So it should be either first or last which are "special" positions.

    So we leave it last, so put 0 and 1 in their optimal location.

Other things that would be cool:

- newline to separate sentences. But maybe this is not needed because we'd send just one sentence per text payload?
- parenthesis to encode open / close pairs, specially for mathematics

## Language

A simplified form of English will be used.

- no plurals
- most punctuation replaced by spaces

### Numbers

Every number is written in binary with `0` and `1`, e.g. 5 == `101`. Never like `zero` or `one`.

#### Negative numbers

TODO One option is to prefix them with `0`, like the Atanasoff Berry computer.

#### Fractions

Fractions are written like in binary with an exponent.

There is no dot `.` to separate fractional and integer parts: integers with exponents are always used.

### Sample sentences

- `0`
- `1`
- `10`: 2
- `11`: 3
- `1 plus 1 equals 10`
- `1 plus 10 equals 11`
- `10 plus 10 equals 100`
- `atom`
- `hydrogen atom`
- `hydrogen atom has 1 electron`
- `hydrogen atom has 1 proton`
- `hydrogen atom has 1 neutron`

To teach them what categories mean, we could send a single word with multiple images members of the category. For example, we'd send the following pairs text image pairs:

- `atom`: schema of a hydrogen atom
- `atom`: schema of a helium atom
- `atom`: schema of a helium atom
