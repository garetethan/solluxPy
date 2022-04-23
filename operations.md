# List of operations
## Native to Python

Use | Explanation
--- | ---
`x + y` |
`x - y` |
`-x` | Negation, AKA unary minus.
`x * y` | Multiplication.
`x ^ y` | Exponentiation. Also aliased as `x ** y` and `pow(x, y)`.
`x / y` |
`x // y` | Floor division, AKA integer division.
`x % y` | [Modulo](https://en.wikipedia.org/wiki/Modulo_operation), AKA the remainder of division.
<code>x &vert; y</code> | [Bit-wise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR).
`x & y` | [Bit-wise AND](https://en.wikipedia.org/wiki/Bitwise_operation#OR).
`min(x, y)` | Minimum.
`max(x, y)` | Maximum.

## Imported
All functions in [Python's math module](https://docs.python.org/3/library/math.html) are available (though, as noted below, some have different names). Here are some I find useful:

Use | Explanation
--- | ---
`sqrt(x)` | The square root of `x` where <code>x &ge; 0</code>.
`log(x)` | The [*natural (base e)* logarithm](https://en.wikipedia.org/wiki/Natural_logarithm) of `x`, where `x > 0`. Also aliased as `ln(x)`.
`log(x, b)` | The base `b` [logarithm](https://en.wikipedia.org/wiki/Logarithm) of `x`, where `b` must be an integer, `b > 1`, and `x > 0`. Also aliased as `logb(x, b)`, `logB(x, b)`, `logc(x, b)`, and `logC(x, b)`.
`lg(x)` | The [binary (base 2) logarithm](https://en.wikipedia.org/wiki/Binary_logarithm) of `x`, where `x > 0`. This is listed in the math module as `log2(x)`, but it can *not* be used this way (because of the way solluxPy supports variables and implicit multiplication). Also aliased as `logTwo(x)`.
`logTen(x)` | The [common (base 10) logarithm](https://en.wikipedia.org/wiki/Common_logarithm) of `x`, where `x > 0`. This is listed in the math module as `log10(x)`, but it can *not* be used this way (because of the way solluxPy supports variables and implicit multiplication).
`factorial(x)` | The [factorial](https://en.wikipedia.org/wiki/Factorial) of `x` where `x` must be an integer and `x > 0`.
`gcd(a, b)` | The [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) of `a` and `b`, where `a` and `b` must be integers.
`floor(x)` | The [floor](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of `x`.
`ceil(x)` | The [ceiling](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of `x`.
`perm(n, k=None)` | The number of [permutations](https://en.wikipedia.org/wiki/Permutation) of `k` elements selected from `n` elements. `k` defaults to `n` if not specified.
`comb(n, k)` | The number of [combinations](https://en.wikipedia.org/wiki/Combination) of `k` elements selected from `n` elements.

### [Trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)

Use | Explanation
--- | ---
`sin(x)` | Sine, where `x` is in radians.
`cos(x)` | Cosine, where `x` is in radians.
`tan(x)` | Tangent, where `x` is in radians.
`asin(x)` | Arcsine, AKA inverse sine, where <code>-1 &le; x &le; 1</code>, `asin(x)` is in radians, and <code>-π / 2 &le; asin(x) &le; π / 2</code>. Also aliased as `arcsin(x)`.
`acos(x)` | Arccosine, AKA inverse cosine, where <code>-1 &le; x &le; 1</code>, `acos(x)` is in radians, and <code>0 &le; acos(x) &le; π</code>. Also aliased as `arccos(x)`.
`atan(x)` | Arctangent, AKA inverse tangent, where `atan(x)` is in radians and <code>-π / 2 &le; atan(x) &le; π / 2</code>. Also aliased as `arctan(x)`.

## Implemented

Use | Explanation
--- | ---
`sq(x)` | Square.
`cb(x)` | Cube.
`root(x, n)` | The real `n`th root of `x` which has the same sign as `x`. Also aliased as `nroot(x, n)`, `rootn(x, n)`, `rootN(x, n)`, and `yroot(x, n)`.
`cbrt(x)` | The real cube root of `x` which has the same sign as `x`.
`quadraticAdd(a, b, c)` | Attempts to find a real solution to ax<sup>2</sup> + bx + c = 0 using the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula) and adding the square root of the discriminant. Does not handle negative discriminants well. Also aliased as `quadraticA(a, b, c)`.
`quadraticSubtract(a, b, c)` | Attempts to find a real solution to ax<sup>2</sup> + bx + c = 0 using the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula) and subtracting the square root of the discriminant. Does not handle negative discriminants well. Also aliased as `quadraticS(a, b, c)` and `quadraticB(a, b, c)`.
`lcm(a, b)` | The [lowest (least) common multiple](https://en.wikipedia.org/wiki/Least_common_multiple), where `a` and `b` must be integers.
`perm(n, k=None)` | *Overwrites math.perm in Python 3.8+.* The number of ways to order `n` items (when `k` is not given), or the number of ways to select `k` items from `n` items when the order of the selected items matters (ie [permutations](https://en.wikipedia.org/wiki/Permutation)). Also aliased as `permutations(n, k)` and `permute(n, k)`.
`comb(n, k)` | *Overwrites math.comb in Python 3.8+.* The number of ways to select `k` items from `n` items when the order of the selected items does not matter (ie [combinations](https://en.wikipedia.org/wiki/Combination)). Also aliased as `combinations(n, k)` and `combine(n, k)`.
`totient(n)` | [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function), where `n` must be an integer.
`divisors(n)` | The [divisor function](https://en.wikipedia.org/wiki/Divisor_function), where `n` must be an integer.

### [Trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)
Use | Explanation
--- | ---
`sec(x)` | Secant, where `x` is in radians.
`csc(x)` | Cosecant, where `x` is in radians.
`cot(x)` | Cotangent, where `x` is in radians.
`asec(x)` | Arcsecant, where `x` is outside the range `(-1, 1)`, `asec(x)` is in radians, and <code>0 &le; asec(x) &le; π</code>. Also aliased as `arcsec(x)`.
`acsc(x)` | Arccosecant, where `x` is outside the range `(-1, 1)`, `acsc(x)` is in radians, and <code>-π / 2 &le; acsc(x) &le; π / 2</code>. Also aliased as `arccsc(x)`.
`acot(x)` | Arccotangent, where `acot(x)` is in radians and <code>-π / 2 &le; acot(x) &le; π / 2</code>. Also aliased as `arccot(x)`.
`sind(x)` | Sine, where `x` is in degrees.
`cosd(x)` | Cosine, where `x` is in degrees.
`tand(x)` | Tangent, where `x` is in degrees.
`secd(x)` | Secant, where `x` is in degrees.
`cscd(x)` | Cosecant, where `x` is in degrees.
`cotd(x)` | Cotangent, where `x` is in degrees.
`asind(x)` | Arcsine, where <code>-1 &le; x &le; 1</code>, `asind(x)` is in degrees, and <code>-90 &le; asind(x) &le; 90</code>. Also aliased as `arcsind(x)`.
`acosd(x)` | Arccosine, where <code>-1 &le; x &le; 1</code>, `acosd(x)` is in degrees, and <code>0 &le; acosd(x) &le; 180</code>. Also aliased as `arccosd(x)`.
`atand(x)` | Arctangent, where `atand(x)` is in degrees and <code>-90 &le; atand(x) &le; 90</code>. Also aliased as `arctand(x)`.
`asecd(x)` | Arcsecant, where `x` is outside the range `(-1, 1)`, `asecd(x)` is in degrees, and <code>0 &le; asecd(x) &le; 180</code>. Also aliased as `arcsecd(x)`.
`acscd(x)` | Arccosecant, where `x` is outside the range `(-1, 1)`, `acscd(x)` is in degrees, and <code>-90 &le; acscd(x) &le; 90</code>. Also aliased as `arccscd(x)`.
`acotd(x)` | Arccotangent, where `acotd(x)` is in degrees and <code>-90 &le; acotd(x) &le; 90</code>. Also aliased as `arccotd(x)`.
