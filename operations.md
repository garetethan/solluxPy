# List of operations
## Native to Python

Use | Clarifications
--- | ---
`x + y` |
`x - y` |
`-x` | Negation, AKA unary minus.
`x * y` |
`x ^ y` | Exponentiation. Also aliased as `x ** y` and `pow(x, y)`.
`x / y` |
`x // y` | Floor division, AKA integer division.
`x % y` | Modulo, AKA the remainder of division.
`x | y` | Bit-wise OR.
`x & y` | Bit-wise AND.

## Imported
All functions in [Python's math module](https://docs.python.org/3/library/math.html) are available (though some as noted below have different names). Here are a few I find useful:

Use | Clarifications
--- | ---
`sqrt(x)` | Square root. Rejects negative numbers.
`sin(x)` | Sine, where `x` is in radians.
`cos(x)` | Cosine, where `x` is in radians.
`tan(x)` | Tangent, where `x` is in radians.
`asin(x)` | Arcsine, AKA inverse sine, where -1 <= `x` <= 1, `asin(x)` is in radians, and -pi / 2 <= `asin(x)` <= pi / 2.
`acos(x)` | Arccosine, AKA inverse cosine, where -1 <= `x` <= 1, `acos(x)` is in radians, and 0 <= `acos(x)` <= pi.
`atan(x)` | Arctangent, AKA inverse tangent, where `atan(x)` is in radians, and -pi / 2 <= `atan(x)` <= pi / 2.
`log(x)` | The *natural (base e)* logarithm of `x`, where `x` > 0. Also aliased as `ln(x)`.
`log(x, b)` | The base `b` logarithm of `x`, where `b` must be an integer, `b` > 1, and `x` > 0. Also aliased as `logb(x, b)`, `logB(x, b)`, `logc(x, b)`, and `logC(x, b)`.
`lg(x)` | The base 2 logarithm of `x`, where `x` > 0. This is listed in the math module as `log2(x)`, but it can *not* be used this way. Also aliased as `logTwo(x)`.
`logTen(x)` | The base 10 logarithm of `x`, where `x` > 0. This is listed in the math module as `log10(x)`, but it can *not* be used this way.
`factorial(x)` | `x` must be an integer and `x` > 0.
`gcd(a, b)` | The greatest common divisor, were `a` and `b` must be integers.
`floor(x)` |
`ceil(x)` | Ceiling.

### New in Python 3.8
These functions are imported from the math module in Python 3.8+, but I have *overwritten* them with my own implementations (that, as far as I know, are identical) because Python 3.8 is [not in Debian Buster yet](https://packages.debian.org/search?suite=buster&keywords=python3.8). The next section defines each of them in more detail.

Use | Clarifications
--- | ---
`perm(n, k=None)` | Permutations.
`comb(n, k)` | Combinations.

## Implemented

Use | Clarifications
--- | ---
`sec(x)` | Secant, where `x` is in radians.
`csc(x)` | Cosecant, where `x` is in radians.
`cot(x)` | Cotangent, where `x` is in radians.
`asec(x)` | Arcsecant, where `x` is outside the range (-1, 1), `asec(x)` is in radians, and 0 <= `asec(x)` <= pi.
`acsc(x)` | Arccosecant, where `x` is outside the range (-1, 1), `acsc(x)` is in radians, and -pi / 2 <= `acsc(x)` <= pi / 2.
`acot(x)` | Arccotangent, where `acot(x)` is in radians and -pi / 2 <= `acot(x)` <= pi / 2.
`sind(x)` | Sine, where `x` is in degrees.
`cosd(x)` | Cosine, where `x` is in degrees.
`tand(x)` | Tangent, where `x` is in degrees.
`secd(x)` | Secant, where `x` is in degrees.
`cscd(x)` | Cosecant, where `x` is in degrees.
`cotd(x)` | Cotangent, where `x` is in degrees.
`asind(x)` | Arcsine, where -1 <= `x` <= 1, `asind(x)` is in degrees, and -90 <= `asind(x)` <= 90.
`acosd(x)` | Arccosine, where -1 <= `x` <= 1, `acosd(x)` is in degrees, and 0 <= `acosd(x)` <= 180.
`atand(x)` | Arctangent, where `atand(x)` is in degrees and -90 <= `atand(x)` <= 90.
`asecd(x)` | Arcsecant, where `x` is outside the range (-1, 1), `asecd(x)` is in degrees, and 0 <= `asecd(x)` <= 180.
`acscd(x)` | Arccosecant, where `x` is outside the range (-1, 1), `acscd(x)` is in degrees, and -90 <= `acscd(x)` <= 90.
`acotd(x)` | Arccotangent, where `acotd(x)` is in degrees and -90 <= `acotd(x)` <= 90.
`sq(x)` | Square.
`cb(x)` | Cube.
`nroot(x)` | The real `n`th root of `x` which has the same sign as `x`. Also aliased as `nthroot(x, n)`, `rootn(x, n)`, `rootN(x, n)`, and `yroot(x, n)`.
`cbrt(x)` | The real cube root of `x` which has the same sign as `x`.
`quadraticAdd(a, b, c)` | Attempts to find a real solution to `a*x^2 + b*x + c = 0` using the quadratic equation and adding the square root of the discriminant. Does not handle negative discriminants well. Also aliased as `quadraticA(a, b, c)`.
`quadraticSubtract(a, b, c)` | Attempts to find a real solution to `a*x^2 + b*x + c = 0` using the quadratic equation and subtracting the square root of the discriminant. Does not handle negative discriminants well. Also aliased as `quadraticS(a, b, c)` and `quadraticB(a, b, c)`.
`lcm(a, b)` | Lowest common multiple, AKA least common multiple, where `a` and `b` must both be integers.
`perm(n, k=None)` | *Overwrites math.perm in Python 3.8+.* The number of ways to order n items (when k is not given), or the number of ways to select k items from n items when the order of the selected items matters. Also aliased as `permutations(n, k)` and `permute(n, k)`.
`comb(n, k)` | *Overwrites math.comb in Python 3.8+.* The number of ways to select k items from n items when the order of the selected items does not matter. Also aliased as `combinations(n, k)` and `combine(n, k)`.
