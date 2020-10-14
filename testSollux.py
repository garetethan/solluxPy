'''
testSollux.py
https://github.com/garetethan/solluxPy
Tests for sollux.py.
'''

from math import pi, sqrt
import re
import subprocess
import unittest

PI_OVER_SIX = pi / 6
PLACES = 4

def run(input_):
	process = subprocess.run(['python3', 'sollux.py'], input=input_ + '\nexit', capture_output=True, text=True)
	if process.stderr:
		# Return the last line of the traceback.
		return process.stderr[:-1].rsplit('\n', maxsplit=1)[1]
	else:
		pattern = 'Enter a mathematical expression to evaluate, a variable declaration, or \'exit\'.\n\n==> _a = ([0-9\\.-]+)\n==> '
		try:
			return float(re.fullmatch(pattern, process.stdout)[1])
		except TypeError:
			return f'Output did not match the expected pattern.\nstdout = {process.stdout}\nstderr = {process.stderr}'

class TestArithmetic(unittest.TestCase):
	def testAddition(self):
		self.assertAlmostEqual(run('3.1 + 4.1'), 7.2, places=PLACES)
	
	def testSubtraction(self):
		self.assertAlmostEqual(run('3.1 - 4.1'), -1, places=PLACES)

	def testMultiplication(self):
		self.assertAlmostEqual(run('3.1 * 4.1'), 12.71, places=PLACES)
	
	def testDivision(self):
		self.assertAlmostEqual(run('3.1 / 4.1'), 31 / 41, places=PLACES)
		self.assertIn('Error: float division by zero', run('3.1 / 0'))

class TestBitwise(unittest.TestCase):
	def testBitwiseOr(self):
		self.assertEqual(run('3 | 4'), 7)
	
	def testBitwiseAnd(self):
		self.assertEqual(run('3 & 4'), 0)
	
class TestTrigonometry(unittest.TestCase):
	def testSec(self):
		self.assertAlmostEqual(run(f'sec({PI_OVER_SIX})'), 2 / sqrt(3), places=PLACES)
	
	def testAsec(self):
		self.assertAlmostEqual(run('asec(2 / sqrt(3))'), PI_OVER_SIX, places=PLACES)
		self.assertIn('Error: math domain error', run('asec(1 / 3)'))
	
	def testSind(self):
		self.assertAlmostEqual(run('sind(30)'), 1 / 2, places=PLACES)
	
	def testSecd(self):
		self.assertAlmostEqual(run('secd(30)'), 2 / sqrt(3), places=PLACES)
	
	def testAsind(self):
		self.assertAlmostEqual(run('asind(1 / 2)'), 30, places=PLACES)
		self.assertIn('Error: math domain error', run('asind(3)'))
	
	def testAsecd(self):
		self.assertAlmostEqual(run('asecd(2 / sqrt(3))'), 30, places=PLACES)
		self.assertIn('Error: math domain error', run('asecd(1 / 3)'))

class TestExponent(unittest.TestCase):
	def testExponentiation(self):
		self.assertEqual(run('3 ^ 4'), 81)
	
	def testSq(self):
		self.assertEqual(run('sq(3)'), 9)
	
	def testCb(self):
		self.assertEqual(run('cb(3)'), 27)
	
	def testSqrt(self):
		self.assertAlmostEqual(run('sqrt(3)') ** 2, 3, places=PLACES)
	
	def testCbrt(self):
		self.assertAlmostEqual(run('cbrt(3)') ** 3, 3, places=PLACES)
	
class TestQuadratic(unittest.TestCase):
	def testQuadraticAdd(self):
		x = run('quadraticA(3.1, 4.1, -5.9)')
		self.assertAlmostEqual(3.1 * x ** 2 + 4.1 * x - 5.9, 0, places=PLACES)
		self.assertIn('Error: math domain error', run('quadraticA(3.1, 4.1, 5.9)'))
	
	def testQuadraticSubtract(self):
		x = run('quadraticS(3.1, 4.1, -5.9)')
		self.assertAlmostEqual(3.1 * x ** 2 + 4.1 * x - 5.9, 0, places=PLACES)
		self.assertIn('Error: math domain error', run('quadraticS(3.1, 4.1, 5.9)'))

class TestLogarithm(unittest.TestCase):
	def testLogB(self):
		self.assertAlmostEqual(3 ** run('log(4, 3)'), 4, places=PLACES)
		self.assertIn('Error: math domain error', run('log(-3, 3)'))
	
	def testLogTen(self):
		self.assertAlmostEqual(10 ** run('logTen(3)'), 3, places=PLACES)
		self.assertIn('Error: math domain error', run('logTen(-3)'))
	
	def testLg(self):
		self.assertAlmostEqual(2 ** run('lg(3)'), 3, places=PLACES)
		self.assertIn('Error: math domain error', run('lg(-3)'))

class TestOther(unittest.TestCase):
	def testLcm(self):
		self.assertEqual(run('lcm(6, 8)'), 24)
	
	def testPerm(self):
		self.assertEqual(run('perm(4, 3)'), 24)
	
	def testComb(self):
		self.assertEqual(run('comb(4, 3)'), 4)

if __name__ == '__main__':
	unittest.main()
