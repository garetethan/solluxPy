# solluxPy
solluxPy is a terminal calculator built with Python. Type in a mathematical expression (not an equation) to have it evaluated. Expression examples:
```
==> 2 + 7
_a = 9
==> sqrt(2)
_b = 1.41421
```
The calculator has the same order of operations as Python, which is probably the order that you expect. Use parentheses (`()`) as necessary, but avoid brackets (`[]`) and braces (`{}`).

## Variables
Notice that each result line in the examples above starts with `_<letter> =`. The calculator is automatically saving each result for you so that you can reference it later in another expression:
```
==> ln(2)
_a = 0.693147
==> _a / ln(3)
_b = 0.63093
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

## Precision
By default all values are printed with six significant digits (even though many more are available), but this can be changed either when starting the program or any time during execution:
```
$ python3 sollux.py -p 12   # set precision to 12
Enter a mathematical expression to evaluate, a variable declaration, or 'exit'.

==> sqrt(2)
_a = 1.41421356237
==> _precision = 3
_b = _precision = 3
==> _a
_c = 1.41
```
## List of operations
See operations.md.

## Name
solluxPy is named after [Sollux Captor](https://mspaintadventures.fandom.com/wiki/Sollux_Captor), a character in [Homestuck](https://www.homestuck.com/).
