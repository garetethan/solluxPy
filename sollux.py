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

from operations import *

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
			result = calc(expression)
			variables[lineVar] = result
			variables['_'] = result
		except (NameError, SyntaxError, ValueError, ZeroDivisionError) as err:
			print(f'Error: {err}')
			continue

		print(f'{lineVar} = ', end='')
		if varName:
			# If any chars in varName are invalid, replace them with underscores.
			varName = re.sub(r'[^a-zA-Z_]', '_', varName)
			variables[varName] = result
			print(f'{varName} = ', end='')
		# bool is a subclass of int
		if isinstance(result, (float, int)) and not isinstance(result, bool):
			print(f'{result:.{variables["_precision"]}g}')
		# The result is not a number.
		else:
			print(result)

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
	varFinder = r'(?<![a-zA-Z_\.])' + VAR_NAME_REGEX + r'(?![a-zA-Z_(])'
	# Insert variable values.
	expression = re.sub(varFinder, lambda m: str(variables[m[0]]), expression)
	return expression

if __name__ == '__main__':
	main()
