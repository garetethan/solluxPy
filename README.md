# pyCalc
Type in a mathematical expression (not an equation) to have it evaluated. Expression examples:
```
==> 2 + 7
_a = 9
==> sqrt(2)
_b = 1.4142135623730951
```
The calculator does respect the normal order of operations (e.g. multiplication before addition). Use parentheses (`()`) as necessary, but avoid brackets (`[]`) and braces (`{}`).

## Variables
Notice that each result line in the examples above starts with `_x =` where `x` is some letter. The calculator is automatically saving each result for you so that you can reference it later in another expression:
```
==> ln(2)
_c = 0.6931471805599453
==> _c / ln(3)
_d = 0.6309297535714574
```
(This will eventually loop around and overwrite old results.)

You can also create your own variables with better names:
```
==> radius = 3.1
_a = radius = 3.1
==> height = 4.1
_b = height = 4.1
==> volume = pi * radius^2 * height
_c = volume = 123.782
```

## List of Operations
### Native to Python

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
`x \| y` | Bit-wise OR.
`x & y` | Bit-wise AND.

### Imported
All functions in [Python's math module](https://docs.python.org/3/library/math.html) are available (though some as noted below have different names). Here are a few I find useful:

Use | Clarifications
--- | ---
`acos(x)` | Arccosine, AKA inverse cosine, where the result is given in radians.
`asin(x)` | Arcsine, AKA inverse sine, where the result is given in radians.
`atan(x)` | Arctangent, AKA inverse tangent, where the result is given in radians.
`ceil(x)` | Ceiling.
`cos(x)` | Cosine, where `x` is given in radians.
`factorial(x)` |
`floor(x)` |
`gcd(a, b)` | The greatest common divisor of `a` and `b`.
`log(x)` | The *natural (base e)* logarithm. Also aliased as `ln(x)`.
`log(x, b)` | The base `b` logarithm of `x`. Also aliased as `logb(x, b)`, `logB(x, b)`, `logc(x, b)`, and `logC(x, b)`.
`lg(x)` | The base 2 logarithm of x. This is listed in the math module as `log2(x)`, but it can *not* be used this way. Also aliased as `logTwo(x)`.
`logTen(x)` | The base 10 logarithm of x. This is listed in the math module as `log10(x)`, but it can *not* be used this way.
`sin(x)` | Sine, where `x` is given in radians.
`sqrt(x)` | Modified to reject negative numbers.
`tan(x)` | Tangent, where `x` is given in radians.

#### New to Python 3.8
These functions are imported from the math module in Python 3.8+, but I have *overwritten* them with my own implementations (that, as far as I know, are identical) because Python 3.8 is not in Debian stable yet. The next section defines each of them in more detail.

Use | Clarifications
--- | ---
`perm(n, k=None)` | Permutations.
`comb(n, k)` | Combinations.

### Implemented

Use | Clarifications
--- | ---
`sec(x)` | Secant, where `x` is given in radians.
`csc(x)` | Cosecant, where `x` is given in radians.
`cot(x)` | Cotangent, where `x` is given in radians.
`asec(x)` | Arcsecant, where the result is given in radians.
`acsc(x)` | Arccosecant, where the result is given in radians.
`acot(x)` | Arccotangent, where the result is given in radians.
`sind(x)` | Sine, where `x` is given in degrees.
`cosd(x)` | Cosine, where `x` is given in degrees.
`tand(x)` | Tangent, where `x` is given in degrees.
`secd(x)` | Secant, where `x` is given in degrees.
`cscd(x)` | Cosecant, where `x` is given in degrees.
`cotd(x)` | Cotangent, where `x` is given in degrees.
`asind(x)` | Arcsine, where the result is given in degrees.
`acosd(x)` | Arccosine, where the result is given in degrees.
`atand(x)` | Arctangent, where the result is given in degrees.
`asecd(x)` | Arcsecant, where the result is given in degrees.
`acscd(x)` | Arccosecant, where the result is given in degrees.
`acotd(x)` | Arccotangent, where the result is given in degrees.
`sq(x)` | Square.
`cb(x)` | Cube.
`nroot(x)` | The `n`th root of x. Also aliased as `nthroot(x, n)`, `rootn(x, n)`, `rootN(x, n)`, and `yroot(x, n)`.
`cbrt(x)` | Cube root.
`quadraticAdd(a, b, c)` | Attempts to find a real solution to `a*x^2 + b*x + c = 0` using the quadratic equation and adding the square root of the discriminant. Does not handle negative discriminants well. Also aliased as `quadraticA(a, b, c)`.
`quadraticSubtract(a, b, c)` | Attempts to find a real solution to `a*x^2 + b*x + c = 0` using the quadratic equation and subtracting the square root of the discriminant. Does not handle negative discriminants well. Also aliased as `quadraticS(a, b, c)` and `quadraticB(a, b, c)`.
`lcm(a, b)` | Lowest common multiple, AKA least common multiple.
`perm(n, k=None)` | *Overwrites math.perm in Python 3.8+.* The number of ways to order n items (when k is not given), or the number of ways to select k items from n items when the order of the selected items matters. Also aliased as `permutations(n, k)` and `permute(n, k)`.
`comb(n, k)` | *Overwrites math.comb in Python 3.8+.* The number of ways to select k items from n items when the order of the selected items does not matter. Also aliased as `combinations(n, k)` and `combine(n, k)`.
