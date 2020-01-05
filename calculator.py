'''
Created on Dec 24, 2017

Written by Garet Robertson.

I want to make a Python calculator around the eval() function.

TODO:
* Consider transforming `(...)!` into `factorial(...)`.
* Prevent the variable parsing from messing with letters in the argument of changeBase(), or consider moving this to a different calculator.
'''

from math import *
from re import fullmatch, sub
from string import ascii_lowercase
from sys import argv

FLOAT_PRECISION = 6
VAR_NAME_REGEX = r'[a-zA-Z_]+'
# Create a space for the user to store numbers temporarily (not between runs).
variables = {'_': 0, 'e': e, 'pi': pi, 'tau': tau}

def main():
	'''Get an expression from the user at the command line. If it is a variable assignment, calc() the right hand side and save it. Otherwise, assume it to be a mathematical expression and print the result of calc()ing it.'''
	global variables

	# First check if any flags were given.
	if len(argv) > 1:
		# 0 - 2 hyphens followed by either 'h' or 'help'.
		if fullmatch(r'-{0,2}h(?:elp)?', argv[1]):
			printHelp()
			return 1
		else:
			print(f'Unrecognized flag (\'{argv[1]}\').')
	
	print('Enter a mathematical expression to evaluate below, or \'quit\'.\n')
	
	expression = ''
	lineNumber = 0
	while True:
		expression = input('==> ')
		lineVar = f'_{ascii_lowercase[lineNumber % 26]}'	
		lineNumber += 1
		if expression.startswith('exit') or expression.startswith('quit'):
			break
		if expression == 'help':
			printHelp()
			continue
		if '=' in expression:
			varName, expression = expression.split('=', maxsplit=1)
			varName = varName.strip()
		else:
			varName = None
		try:
			expression = insertVars(expression)
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
			if not fullmatch(VAR_NAME_REGEX, varName):
				varName = sub(r'[^a-zA-Z_]', '_', varName)
			variables[varName] = variables[lineVar]
			print(f'{lineVar} = {varName} = {variables[lineVar]:.{FLOAT_PRECISION}g}')
		else:
			print(f'{lineVar} = {variables[lineVar]:.{FLOAT_PRECISION}g}')
		
	return 0

def insertVars(expression):
	'''Replace variable names with their values in expression.'''
	# Make implicit multiplication between coefficients and variables explicit.
	expression = sub(r'(\d)([a-zA-Z_])', r'\1*\2', expression)
	# Insert variable values.
	varFinder = VAR_NAME_REGEX + r'(?![a-zA-Z_(])'
	expression = sub(varFinder, lambda m: str(variables[m[0]]), expression)
	return expression

def calc(expression):
	'''Evaluate a string expression (returning a float). Do not catch any exceptions.'''
	
	# Replace absolute-value bars with the abs() function that eval() will recognize.
	# Assumes that absolute-value bars are never nested. (If they were it would likely make the expression ambiguous.)
	expression = sub(r'\|(.*?)\|', r'abs(\1)', expression)
	# Replace 3! with factorial(3). Does not bother trying to match non-integers since factorial() would reject them anyways.
	expression = sub(r'(\d+)!', r'factorial(\1)', expression)
	# Replace '^' (Python XOR) with '**' (exponentiation) and ')(' with ')*(' (implicit multiplication).
	replacements = {'^': '**', ')(': ')*('}
	for old in replacements:
		expression = expression.replace(old, replacements[old])
	
	# Let Python evaluate the filtered mathematical expression.
	return eval(expression)

# Define missing trig functions.
def sec(num):
	return 1 / cos(num)

def csc(num):
	return 1 / sin(num)

def cot(num):
	return 1 / tan(num)

def asec(num):
	return acos(1 / num)

def acsc(num):
	return asin(1 / num)

def acot(num):
	return acot(1 / num)

# Define trig functions that assume inputs are in degrees.
def sind(num):
	return sin(radians(num))

def cosd(num):
	return cos(radians(num))

def tand(num):
	return tan(radians(num))

def secd(num):
	return 1 / cos(radians(num))

def cscd(num):
	return 1 / sin(radians(num))

def cotd(num):
	return 1 / tan(radians(num))

# Define arc (inverse) trig functions that convert outputs to degrees.
def asind(num):
	return degrees(asin(num))

def acosd(num):
	return degrees(acos(num))

def atand(num):
	return degrees(atan(num))

def asecd(num):
	return degrees(acos(1 / num))

def acscd(num):
	return degrees(asin(1 / num))

def acotd(num):
	return degrees(atan(1 / num))

def sq(num):
	'''Square.'''
	return num ** 2

def cb(num):
	'''Cube.'''
	return num ** 3

def cbrt(num):
	'''Cube root.'''
	return num ** (1 / 3)

def quadraticAdd(a, b, c):
	'''Attempt to solve ax^2 + bx + c = 0, adding the square root of the discriminant in the quadratic equation. Do not give solutions with a non-zero imaginary component.'''
	return -b + sqrt(sq(b) - 4 * a * c) / 2 * a
quadraticA = quadraticAdd

# Subtracts discriminant.
def quadraticSubtract(a, b, c):
	'''Attempt to solve ax^2 + bx + c = 0, subtracting the square root of the discriminant in the quadratic equation. Do not give solutions with a non-zero imaginary component.'''
	return -b - sqrt(sq(b) - 4 * a * c) / 2 * a
quadraticS = quadraticSubtract
quadraticB = quadraticSubtract

ln = log

def logB(num, base):
	'''General logarithm. The letter b is used to represent the base because of [its use on Wikipedia](https://en.wikipedia.org/wiki/Logarithm).'''
	# Change-of-base formula.
	return ln(num) / ln(base)
logC = logB
logX = logB

def logTen(num):
	'''Base 10 logarithm.'''
	return logB(num, 10)

def lg(num):
	'''Base 2 logarithm.'''
	return logC(num, 2)
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

def comb(n, k):
	'''Combinations.'''
	if k <= n:
		return factorial(n) / (factorial(k) * factorial(n - k))
	else:
		return 0
combinations = comb

def printHelp():
	with open('README.md', 'r') as helpFile:
		for line in helpFile:
			print(line, end='')

if __name__ == '__main__':
	main()
