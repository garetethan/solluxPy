# pyCalc
Type in a mathematical expression (not an equation) to have it evaluated. Expression examples:
```
==> 2 + 7
_a = 9
==> sqrt(2)
_b = 1.4142135623730951
```
Use parentheses to control the order of operations.

## Variables
Notice that each result line starts with `_x = ` where x is some letter. The calculator is automatically saving each result for you so that you can reference it later in another expression:
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
`x + y` |
`x - y` | 
`-x` | Negation, AKA unary minus.
`x * y` |
`x ** y` | Exponentiation. Also aliased as `x ^ y` and `pow(x, y)`.
`x / y` |
`x // y` | Floor division, AKA integer division.
`x % y` | Modulo, AKA the remainder of division.

### Imported
All functions in [Python's math module](https://docs.python.org/3/library/math.html) are available. A few of the common ones are listed here.
`ceil(x)` | Ceiling.
`comb(n, k)` | The number of ways to select k items from n items when the order of the selected items does not matter. Also aliased as `combinations(n, k)`.
`factorial(x)` |
`floor(x)` |
`perm(n, k=None)` | The number of ways to order n items, or the number of ways to select k items from n items when the order of the selected items matters. Also aliased as `permutations(n, k)`.
`log(x)` | The *natural (base e)* logarithm. Also aliased as `ln(x)`.
`log(x, b)` | The base b logarithm of x. Also aliased as `logB(x, b)`, `logC(x, b)`, and `logX(x, b)`.
`lg(x)` | The base 2 logarithm of x. This is listed in the math module as `log2(x)`, but it can *not* be used this way.
`logTen(x)` | The base 10 logarithm of x. This is listed in the math module as `log10(x)`, but it can *not* be used this way.

### Implemented


