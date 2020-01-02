'''
Created on Dec 24, 2017

Written by Garet Robertson.

I want to make a Python calculator around the eval() function.

TODO:
* Make a factorize or unmultiply function.
* Once you get most of the other things working, I would like to be able to map keys on my keyboard to different things so that I do not have to use all of keys around the edge to type in a mathematical expression. (I don't know if there would be a good way to do this, though.)
* math domain error is handled in sqrt(), but also needs to be handled in log().
* So I don't think I understand this completely, but I think that, because of the way I am using Decimals, they are imprecise, and therefore offer no clear advantage over just using floats. This is because I am allowing eval() to convert a string like '-2' or '3 + 5' into the number -2 and 8, respectively, before Decimal() ever gets a hold of them. I need to find a way to turn all numbers into decimals before anything else happens to them.
* Consider transforming (...)! into factorial(...).
'''

from math import *
# Necessary for DISALLOWED_VAR_NAMES below.
import math
from re import *
from sys import argv
from string import ascii_lowercase, ascii_uppercase, digits
from pprint import pprint

FLOAT_PRECISION = 6
VAR_NAME_REGEX = r'[a-zA-Z_]+'
DISALLOWED_VAR_NAMES = [i for i in dir(math) if i[0] != '_']
DISALLOWED_VAR_NAMES.extend(['quit', 'exit', 'help', 'ops', 'e', 'pi', 'tau', 'sec', 'csc', 'cot', 'asec', 'acsc', 'acot', 'sind', 'cosd', 'tand', 'secd', 'cscd', 'cotd', 'asind', 'acosd', 'atand', 'asecd', 'acscd', 'acotd', 'sq', 'cb', 'cbrt', 'quadraticA', 'quadraticS', 'ln', 'logB', 'logC', 'logX', 'logTen', 'lg', 'exp', 'lcm', 'permute', 'choose', 'changeBase', 'printHelp', 'printOps'])
# Create a space for the user to store numbers temporarily (not between runs).
variables = {'_': 0, 'e': e, 'pi': pi, 'tau': tau}

def textDriver():
	'''Get an expression from the user at the command line. If it is a variable assignment, calc() the right hand side and save it. Otherwise, assume it to be a mathematical expression and print the result of calc()ing it.'''
	# First check if any flags were given.
	if len(argv) > 1:
		if argv[1] == 'help':
			printHelp()
			return 1
		
		if argv[1] == 'ops':
			printOps()
			return 2
	
	print('Enter a mathematical expression to evaluate below, or \'quit\'.\n')
	
	# Identical line at the end of the following while loop.
	expression = input('==> ')
	lineNumber = 0
	while not expression.startswith('quit') and not expression.startswith('exit'):
		lineVar = f'_{ascii_lowercase[lineNumber % 26]}'	
		if expression == 'help':
			printHelp()
		elif expression == 'ops':
			printOps()
		
		# If it is a variable assignment, save the value
		elif '=' in expression:
			varName, varValue = expression.split('=', maxsplit=1)
			varName = varName.strip()
			varValue = insertVars(varValue)
			if varName in DISALLOWED_VAR_NAMES:
				print(f'That name is not allowed because the math module has a variable or a method by that name.')
			# As long as insertVars() was successful.
			elif varValue:
				if not fullmatch(VAR_NAME_REGEX, varName):
					varName = sub(r'[^a-zA-Z_]', r'_', varName)
				try:
					variables[varName] = calc(varValue)
					variables[lineVar] = variables[varName]
					variables['_'] = variables[varName]
					print(f'{lineVar} = {varName} = {variables[lineVar]:.{FLOAT_PRECISION}g}')
				except NameError as err:
					print(f'Error: {err}')
		# Else it should be a mathematical expression to be evaluated (but it might include references to variables that have to be replaced with values).
		else:
			expression = insertVars(expression)
			if expression:
				try:
					variables[lineVar] = calc(expression)
					variables['_'] = variables[lineVar]
					print(f'{lineVar} = {variables[lineVar]:.{FLOAT_PRECISION}g}')
				except (NameError, SyntaxError, ZeroDivisionError) as err:
					print(f'Error: {err}')
		
		# Get input for next run.
		expression = input('==> ')
		lineNumber += 1
	
	return 0

def insertVars(expression):
		# Make implicit multiplication between coefficients and variables explicit.
		expression = sub(r'(\d)([a-zA-Z_])', r'\1*\2', expression)
		# Insert variable values.
		varFinder = VAR_NAME_REGEX + r'(?![a-zA-Z_(])'
		try:
			expression = sub(varFinder, lambda m: str(variables[m[0]]), expression)
			return expression
		except KeyError as err:
			print(f'There is no variable called {err}.')
			return None

def calc(expression):
	'''Evaluate a string expression. Do not catch any exceptions.'''
	
	# Replace absolute-value bars with the abs() function that eval() will recognize.
	# Assumes that absolute-value bars are never nested (which is impossible to tell for sure).
	expression = sub(r'\|(.*?)\|', r'abs(\1)', expression)
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

# Square, cube, and cuberoot.
def sq(num):
	return num ** 2

def sqrt(num):
	'''Return the positive square root of any positive, real number.
	Defined here (overwriting the math module) just so that we can print a statement in the case of negative input.'''
	try:
		return math.sqrt(num)
	except ValueError as err:
		print('Square root of a negative encountered. This calculator does not support imaginary numbers, so the square root of the absolute value of the given value has been used instead.')
		return math.sqrt(-num)

def cb(num):
	return num ** 3

def cbrt(num):
	return num ** (1 / 3)

# Quadratic formula
# Adds discriminant.
def quadraticA(a, b, c):
	return -b + sqrt(sq(b) - 4 * a * c) / 2 * a

# Subtracts discriminant.
def quadraticS(a, b, c):
	return -b - sqrt(sq(b) - 4 * a * c) / 2 * a

# This a function alias, not a variable declaration.
ln = log

# The letter b is used to represent the base because of [its use on Wikipedia](https://en.wikipedia.org/wiki/Logarithm).
def logB(num, base):
	# Change-of-base formula.
	return ln(num) / ln(base)

logC = logB
logX = logB

def logTen(num):
	return logB(num, 10)

def lg(num):
	return logC(num, 2)

def lcm(a, b):
	'''Lowest common multiple.'''
	return a * b / gcd(a, b)

permutations = perm
combinations = comb

def changeBase(num, oldBase, newBase):
	'''Should not be used in combination with other functions in the same statement (because it returns a string not necessarily parsable as a float).
	num is assumed to be a string representation of an integer, and oldBase and newBase integers.'''
	
	# From oldBase to base 10.
	num = int(num, oldBase)

	# From base 10 to newBase.
	if newBase == 10:
		return num
	else:
		# Define list of symbols used as digits
		# Lists of chars come from the string module.
		symbols = digits + ascii_uppercase
	
		# Uses "the division method"
		isNeg = oldNum < 0
		oldNum = abs(oldNum)
		newNum = ''
		while oldNum:
			newNum = f'{symbols[oldNum % newBase]}{newNum}'
			oldNum //= newBase
		if isNeg:
			newNum = f'-{newNum}'
		return newNum

def printHelp():
	with open('README.md', 'r') as helpFile:
		for line in helpFile:
			if line[0] != '#':
				print(line, end='')

if __name__ == '__main__':
	textDriver()
