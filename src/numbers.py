'''
Created on 19/05/2010

@author: Guga
'''
import math
import primes
import unittest

def getDigits(number):
    quocient = abs(number) // 10
    remain = abs(number) % 10
    digits = [remain]
    while (quocient > 0):
        remain = quocient % 10
        quocient = quocient // 10
        digits.insert(0, remain)
    return digits

'''
@see: http://en.wikipedia.org/wiki/Power_of_two#Fast_algorithm_to_check_if_a_positive_number_is_a_power_of_two
'''
def isPowerOfTwo(x):
    y = x - 1
    return x & y == 0

def simplifyNumber(number, factor, callback = None):
    while number % factor == 0:
        number /= factor
        if callback != None:
            callback(number)
    return number

class PrimeFactors:
    def __init__(self, primeGenerator = None):
        # cache of the form: dict(number => dict ( factor => times it factors 'number' ) )
        self.cache = dict()

        if primeGenerator is None:
            self.primeGenerator = primes.PrimeGenerator()
        else:
            self.primeGenerator = primeGenerator

    def getPrimeFactors(self, number, callback = None):

        countedPrimes = self.getCountedPrimeFactors(number)
        return list(countedPrimes.keys())

    def getCountedPrimeFactors(self, number):
        '''
        Returns a dict() at the form:
        
        factor => times it factors the <param>number</param>
        '''

        possibleDivisors = self.primeGenerator.primeListUsingSieveOfEratosthenes(int(math.sqrt(number) + 1))

        if number == 1:
            # the number will get simplified to 1, so we need to add this case of the recursion
            return None

        if number in self.cache:
            return self.cache[number]

        # Optimization for prime numbers
        if self.primeGenerator.isPrime(number):
            return dict([(number, 1)])

        for possibleDivisor in possibleDivisors:
            if possibleDivisor > number:
                raise RuntimeError("IsPrime is bugged!")

            if number % possibleDivisor == 0:
                primeFactors = dict()

                def inc(x):
                    if x in primeFactors:
                        primeFactors[x] += 1
                    else:
                        primeFactors[x] = 1

                theCallback = lambda x : inc(possibleDivisor)
                simplifiedNumber = simplifyNumber(number, possibleDivisor, theCallback)
                others = self.getCountedPrimeFactors(simplifiedNumber)
                if others != None:
                    primeFactors.update(others)
                self.cache[number] = primeFactors

                return primeFactors

        raise RuntimeError("Couldn't find a prime that divides the number. That's odd :(")


class Test(unittest.TestCase):

    def setUp(self):
        self.primeFactors = PrimeFactors()

    def testGetDigits(self):
        self.assertEqual([4, 3, 2, 1], getDigits(4321))

    def testGetPrimeFactors(self):
        self.assertEqual([2], self.primeFactors.getPrimeFactors(2))
        self.assertEqual([3], self.primeFactors.getPrimeFactors(3))
        self.assertEqual([2], self.primeFactors.getPrimeFactors(4))
        self.assertEqual([5], self.primeFactors.getPrimeFactors(5))
        self.assertEqual([2, 3], self.primeFactors.getPrimeFactors(6))
        self.assertEqual([2, 3], self.primeFactors.getPrimeFactors(12))

    def testGetCountedPrimeFactors(self):
        self.assertEqual(dict([(2, 1)]), self.primeFactors.getCountedPrimeFactors(2))
        self.assertEqual(dict([(3, 1)]), self.primeFactors.getCountedPrimeFactors(3))
        self.assertEqual(dict([(2, 2)]), self.primeFactors.getCountedPrimeFactors(4))
        self.assertEqual(dict([(5, 1)]), self.primeFactors.getCountedPrimeFactors(5))
        self.assertEqual(dict([(2, 1), (3, 1)]), self.primeFactors.getCountedPrimeFactors(2 ** 1 * 3 ** 1))
        self.assertEqual(dict([(2, 2), (3, 1)]), self.primeFactors.getCountedPrimeFactors(2 ** 2 * 3 ** 1))
        self.assertEqual(dict([(2, 2), (3, 2)]), self.primeFactors.getCountedPrimeFactors(2 ** 2 * 3 ** 2))
