import math

# Aliases of provided trig functions.
arcsin = math.asin
arccos = math.acos
arctan = math.atan

# Define missing trig functions.
def sec(x):
	'''Secant.'''
	return 1 / math.cos(x)

def csc(x):
	'''Cosecant.'''
	return 1 / math.sin(x)

def cot(x):
	'''Cotangent.'''
	return 1 / math.tan(x)

def asec(x):
	'''Arcsecant.'''
	return math.acos(1 / x)
arcsec = asec

def acsc(x):
	'''Arccosecant.'''
	return math.asin(1 / x)
arccsc = acsc

def acot(x):
	'''Arccotangent.'''
	if x == 0:
		return -math.pi / 2
	else:
		return math.atan(1 / x)
arccot = acot

# Define trig functions that assume inputs are in degrees.
def sind(x):
	'''Sine (degrees).'''
	return math.sin(math.radians(x))

def cosd(x):
	'''Cosine (degrees).'''
	return math.cos(math.radians(x))

def tand(x):
	'''Tangent (degrees).'''
	return math.tan(math.radians(x))

def secd(x):
	'''Secant (degrees).'''
	return sec(math.radians(x))

def cscd(x):
	'''Cosecant (degrees).'''
	return csc(math.radians(x))

def cotd(x):
	'''Cotangent (degrees).'''
	return cot(math.radians(x))

# Define arc (inverse) trig functions that convert outputs to degrees.
def asind(x):
	'''Arcsine (degrees).'''
	return math.degrees(math.asin(x))
arcsind = asind

def acosd(x):
	'''Arccosine (degrees).'''
	return math.degrees(math.acos(x))
arccosd = acosd

def atand(x):
	'''Arctangent (degrees).'''
	return math.degrees(math.atan(x))
arctand = atand

def asecd(x):
	'''Arcsecant (degrees).'''
	return math.degrees(asec(x))
arcsecd = asecd

def acscd(x):
	'''Arccosecant (degrees).'''
	return math.degrees(acsc(x))
arccscd = acscd

def acotd(x):
	'''Arccotangent (degrees).'''
	return math.degrees(acot(x))
arccotd = acotd

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
	return (-b + math.sqrt(sq(b) - 4 * a * c)) / (2 * a)
quadraticA = quadraticAdd

def quadraticSubtract(a, b, c):
	'''Attempt to solve ax^2 + bx + c = 0, subtracting the square root of the discriminant in the quadratic equation. Do not give solutions with a non-zero imaginary component.'''
	return (-b - math.sqrt(sq(b) - 4 * a * c)) / (2 * a)
quadraticS = quadraticSubtract
quadraticB = quadraticSubtract

ln = math.log

def logb(x, b):
	'''General logarithm. `b` is used to represent the base because of [its use on Wikipedia](https://en.wikipedia.org/wiki/Logarithm).'''
	return ln(x) / ln(b)
logB = logb
logc = logb
logC = logb

def logTen(x):
	'''Base 10 logarithm.'''
	return logb(x, 10)

def lg(x):
	'''Base 2 logarithm.'''
	return logb(x, 2)
logTwo = lg

def lcm(a, b):
	'''Lowest common multiple.'''
	return a * b / math.gcd(a, b)

def perm(n, k=None):
	'''Permutations. perm and comb are defined in math in Python 3.8, but I have defined them separately here because Debian stable's latest version of Python is still 3.7 (2020-01-04).'''
	if k is None:
		return math.factorial(n)
	elif k <= n:
		return math.factorial(n) / math.factorial(n - k)
	else:
		return 0
permutations = perm
permute = perm

def comb(n, k):
	'''Combinations.'''
	if k <= n:
		return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
	else:
		return 0
choose = comb
combinations = comb
combine = comb

def totient(n):
	return sum(1 if math.gcd(n, k) == 1 else 0 for k in range(1, n))

def divisors(n):
	return sum(1 if n % k == 0 else 0 for k in range(1, n + 1))
