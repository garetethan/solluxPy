'''
testSollux.py
https://github.com/garetethan/solluxPy
Tests for sollux.py.
'''

from unittest import main, TestCase
from sollux import calc
from math import pi, sqrt

PI_OVER_SIX = pi / 6

class TestArithmetic(TestCase):
	def testAddition(self):
		self.assertAlmostEqual(calc('3.1 + 4.1'), 7.2)
	
	def testSubtraction(self):
		self.assertAlmostEqual(calc('3.1 - 4.1'), -1)

	def testMultiplication(self):
		self.assertAlmostEqual(calc('3.1 * 4.1'), 12.71)
	
	def testDivision(self):
		self.assertAlmostEqual(calc('3.1 / 4.1'), 31 / 41)
		self.assertRaises(ZeroDivisionError, calc, '3.1 / 0')

class TestBitwise(TestCase):
	def testBitwiseOr(self):
		self.assertEqual(calc('3 | 4'), 7)
	
	def testBitwiseAnd(self):
		self.assertEqual(calc('3 & 4'), 0)
	
class TestTrigonometry(TestCase):
	def testSec(self):
		self.assertAlmostEqual(calc(f'sec({PI_OVER_SIX})'), 2 / sqrt(3))
	
	def testAsec(self):
		self.assertAlmostEqual(calc('asec(2 / sqrt(3))'), PI_OVER_SIX)
		self.assertRaises(ValueError, calc, 'asec(1 / 3)')
	
	def testSind(self):
		self.assertAlmostEqual(calc('sind(30)'), 1 / 2)
	
	def testSecd(self):
		self.assertAlmostEqual(calc('secd(30)'), 2 / sqrt(3))
	
	def testAsind(self):
		self.assertAlmostEqual(calc('asind(1 / 2)'), 30)
		self.assertRaises(ValueError, calc, 'asind(3)')
	
	def testAsecd(self):
		self.assertAlmostEqual(calc('asecd(2 / sqrt(3))'), 30)
		self.assertRaises(ValueError, calc, 'asecd(1 / 3)')

class TestExponent(TestCase):
	def testExponentiation(self):
		self.assertEqual(calc('3 ^ 4'), 81)
	
	def testSq(self):
		self.assertEqual(calc('sq(3)'), 9)
	
	def testCb(self):
		self.assertEqual(calc('cb(3)'), 27)
	
	def testSqrt(self):
		self.assertAlmostEqual(calc('sqrt(3)') ** 2, 3)
	
	def testCbrt(self):
		self.assertAlmostEqual(calc('cbrt(3)') ** 3, 3)
	
class TestQuadratic(TestCase):
	def testQuadraticAdd(self):
		x = calc('quadraticA(3.1, 4.1, -5.9)')
		self.assertAlmostEqual(3.1 * x ** 2 + 4.1 * x - 5.9, 0)
		self.assertRaises(ValueError, calc, 'quadraticA(3.1, 4.1, 5.9)')
	
	def testQuadraticSubtract(self):
		x = calc('quadraticS(3.1, 4.1, -5.9)')
		self.assertAlmostEqual(3.1 * x ** 2 + 4.1 * x - 5.9, 0)
		self.assertRaises(ValueError, calc, 'quadraticS(3.1, 4.1, 5.9)')

class TestLogarithm(TestCase):
	def testLogB(self):
		self.assertAlmostEqual(3 ** calc('log(4, 3)'), 4)
		self.assertRaises(ValueError, calc, 'log(-3, 3)')
	
	def testLogTen(self):
		self.assertAlmostEqual(10 ** calc('logTen(3)'), 3)
		self.assertRaises(ValueError, calc, 'logTen(-3)')
	
	def testLg(self):
		self.assertAlmostEqual(2 ** calc('lg(3)'), 3)
		self.assertRaises(ValueError, calc, 'lg(-3)')

class TestOther(TestCase):
	def testLcm(self):
		self.assertEqual(calc('lcm(6, 8)'), 24)
	
	def testPerm(self):
		self.assertEqual(calc('perm(4, 3)'), 24)
	
	def testComb(self):
		self.assertEqual(calc('comb(4, 3)'), 4)

if __name__ == '__main__':
	main()
