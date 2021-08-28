'''
sollux.py
https://github.com/garetethan/solluxPy
Created on 2017-12-24.

TODO:
* Improve the replacement of `!` with `factorial(...)`.
'''

import argparse
from math import *
import re
import string
from sys import argv

PRECISION_DEFAULT = 9
PRECISION_DESCRIPTION = f'the number of significant figures to print (default {PRECISION_DEFAULT})'

VAR_NAME_REGEX = r'[a-zA-Z_]+'

def main():
	'''Get an expression from the user at the command line. If it is a variable assignment, evaluate the right hand side and save it. Otherwise, assume it to be a mathematical expression, evaluate it, and save and print the result.'''
	# Create a space for the user to store numbers temporarily.
	# '_' stores the last calculated result, and '_precision' limits how many digits of floating point results are printed.
	variables = {'_': 0, 'e': e, 'pi': pi, 'tau': tau}

	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--operations', '-f', '--functions', action='store_true', help='print the full list of supported operations (ie functions) and exit')
	parser.add_argument('-p', '--precision', default=PRECISION_DEFAULT, type=int, help=PRECISION_DESCRIPTION, metavar='N')
	args = parser.parse_args()

	if args.operations:
		with open('operations.md') as operationsFile:
			print(operationsFile.read())
			raise SystemExit()

	variables['_precision'] = args.precision
	print('Enter a mathematical expression to evaluate, a variable declaration, or \'exit\'.\n')

	expression = ''
	lineNumber = 0
	while True:
		expression = input('==> ')
		lineVar = f'_{string.ascii_lowercase[lineNumber % 26]}'
		lineNumber += 1
		if expression.startswith('exit') or expression.startswith('quit'):
			break
		if expression == 'help':
			print('Type an expression, like:\n37 / 3\nor:\n(3 - 4) * sin(pi / 2)')
			continue
		if '=' in expression:
			varName, expression = expression.split('=', maxsplit=1)
			varName = varName.strip()
		else:
			varName = None
		try:
			expression = insertVars(expression, variables)
		except KeyError as err:
			print(f'There is no variable called {err}.')
			continue
		try:
			variables[lineVar] = calc(expression)
			variables['_'] = variables[lineVar]
		except (NameError, SyntaxError, ValueError, ZeroDivisionError) as err:
			print(f'Error: {err}')
			continue
		if varName:
			# If any chars in varName are invalid, replace them with underscores.
			varName = re.sub(r'[^a-zA-Z_]', '_', varName)
			variables[varName] = variables[lineVar]
			print(f'{lineVar} = {varName} = {variables[lineVar]:.{variables["_precision"]}g}')
		else:
			print(f'{lineVar} = {variables[lineVar]:.{variables["_precision"]}g}')

	return 0

def calc(expression):
	'''Evaluate a string expression (returning a float). Do not catch any exceptions.'''

	# Replace absolute-value bars with the abs() function that eval() will recognize.
	# Assumes that absolute-value bars are never nested. (If they were it would likely make the expression ambiguous.)
	expression = re.sub(r'\|(.*?)\|', r'abs(\1)', expression)
	# Replace <int>! with factorial(<int>). Does not bother trying to match non-integers since factorial() would reject them anyways.
	expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)
	# Replace '^' (Python XOR) with '**' (exponentiation) and ')(' with ')*(' (implicit multiplication).
	replacements = {'^': '**', ')(': ')*('}
	for old in replacements:
		expression = expression.replace(old, replacements[old])

	# Let Python evaluate the filtered mathematical expression.
	return eval(expression)

def insertVars(expression, variables):
	'''Replace variable names with their values in expression.'''
	# Make implicit multiplication between coefficients and functions and variables explicit.
	expression = re.sub(r'(\d)([a-zA-Z_])', r'\1*\2', expression)
	# Look for a variable name followed by anything but '('.
	varFinder = VAR_NAME_REGEX + r'(?![a-zA-Z_(])'
	# Insert variable values.
	expression = re.sub(varFinder, lambda m: str(variables[m[0]]), expression)
	return expression

# Define missing trig functions.
def sec(x):
	'''Secant.'''
	return 1 / cos(x)

def csc(x):
	'''Cosecant.'''
	return 1 / sin(x)

def cot(x):
	'''Cotangent.'''
	return 1 / tan(x)

def asec(x):
	'''Arcsecant.'''
	return acos(1 / x)

def acsc(x):
	'''Arccosecant.'''
	return asin(1 / x)

def acot(x):
	'''Arccotangent.'''
	if x == 0:
		return -pi / 2
	else:
		return atan(1 / x)

# Define trig functions that assume inputs are in degrees.
def sind(x):
	'''Sine (degrees).'''
	return sin(radians(x))

def cosd(x):
	'''Cosine (degrees).'''
	return cos(radians(x))

def tand(x):
	'''Tangent (degrees).'''
	return tan(radians(x))

def secd(x):
	'''Secant (degrees).'''
	return sec(radians(x))

def cscd(x):
	'''Cosecant (degrees).'''
	return csc(radians(x))

def cotd(x):
	'''Cotangent (degrees).'''
	return cot(radians(x))

# Define arc (inverse) trig functions that convert outputs to degrees.
def asind(x):
	'''Arcsine (degrees).'''
	return degrees(asin(x))

def acosd(x):
	'''Arccosine (degrees).'''
	return degrees(acos(x))

def atand(x):
	'''Arctangent (degrees).'''
	return degrees(atan(x))

def asecd(x):
	'''Arcsecant (degrees).'''
	return degrees(asec(x))

def acscd(x):
	'''Arccosecant (degrees).'''
	return degrees(acsc(x))

def acotd(x):
	'''Arccotangent (degrees).'''
	return degrees(acot(x))

def sq(x):
	'''Square.'''
	return x ** 2

def cb(x):
	'''Cube.'''
	return x ** 3

def root(x, n):
	'''The `n`th root of x. `n` is used to represent the degree of the root because of [its use on Wikipedia](https://en.wikipedia.org/wiki/Nth_root).'''
	return x ** (1 / n)
nroot = root
rootn = root
rootN = root
yroot = root

def cbrt(x):
	'''Cube root.'''
	return x ** (1 / 3)

def quadraticAdd(a, b, c):
	'''Attempt to solve ax^2 + bx + c = 0, adding the square root of the discriminant in the quadratic equation. Do not give solutions with a non-zero imaginary component.'''
	return (-b + sqrt(sq(b) - 4 * a * c)) / (2 * a)
quadraticA = quadraticAdd

# Subtracts discriminant.
def quadraticSubtract(a, b, c):
	'''Attempt to solve ax^2 + bx + c = 0, subtracting the square root of the discriminant in the quadratic equation. Do not give solutions with a non-zero imaginary component.'''
	return (-b - sqrt(sq(b) - 4 * a * c)) / (2 * a)
quadraticS = quadraticSubtract
quadraticB = quadraticSubtract

ln = log

def logb(x, b):
	'''General logarithm. `b` is used to represent the base because of [its use on Wikipedia](https://en.wikipedia.org/wiki/Logarithm).'''
	return ln(x) / ln(b)
logB = logb
logc = logb
logC = logb

def logTen(x):
	'''Base 10 logarithm.'''
	return logB(x, 10)

def lg(x):
	'''Base 2 logarithm.'''
	return logC(x, 2)
logTwo = lg

def lcm(a, b):
	'''Lowest common multiple.'''
	return a * b / gcd(a, b)

# perm and comb are defined in math in Python 3.8, but I have defined them separately here because Debian stable's latest version of Python is still 3.7 (2020-01-04).
def perm(n, k=None):
	'''Permutations.'''
	if k is None:
		return factorial(n)
	elif k <= n:
		return factorial(n) / factorial(n - k)
	else:
		return 0
permutations = perm
permute = perm

def comb(n, k):
	'''Combinations.'''
	if k <= n:
		return factorial(n) / (factorial(k) * factorial(n - k))
	else:
		return 0
choose = comb
combinations = comb
combine = comb

if __name__ == '__main__':
	main()
