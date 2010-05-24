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

def simplifyNumber(number, factor, callback=None):
    while number % factor == 0:
        number /= factor
        if callback != None:
            callback(number)
    return number

def getPrimeFactors(number, primeGenerator=None, callback=None):
    primeFactors = []
    
    if primeGenerator is None:
        primeGenerator = primes.PrimeGenerator()
        
    possibleDivisors = primeGenerator.primeListUsingSieveOfEratosthenes(number)
    
    for possibleDivisor in possibleDivisors:
        if possibleDivisor > number:
            break
        
        if number % possibleDivisor == 0:
            theCallback = None
            if callback is not None:
                theCallback = lambda x : callback(possibleDivisor)
            
            number = simplifyNumber(number, possibleDivisor, theCallback)
            primeFactors.append(possibleDivisor)
         
    return primeFactors

def getCountedPrimeFactors(number, primeGenerator=None):
    countedPrimeFactors = dict()
    
    def inc(x):
        if x in countedPrimeFactors:
            countedPrimeFactors[x] += 1
        else:
            countedPrimeFactors[x] = 1
        
    getPrimeFactors(number, primeGenerator, inc)
    
    return countedPrimeFactors

class Test(unittest.TestCase):
    def testGetDigits(self):
        self.assertEqual([4, 3, 2, 1], getDigits(4321))
        
    def testGetPrimeFactors(self):
        self.assertEqual([2], getPrimeFactors(2))
        self.assertEqual([3], getPrimeFactors(3))
        self.assertEqual([2], getPrimeFactors(4))
        self.assertEqual([5], getPrimeFactors(5))
        self.assertEqual([2, 3], getPrimeFactors(6))
        self.assertEqual([2, 3], getPrimeFactors(12))
        
    def testGetCountedPrimeFactors(self):
        self.assertEqual(dict([(2, 1)]), getCountedPrimeFactors(2))
        self.assertEqual(dict([(3, 1)]), getCountedPrimeFactors(3))
        self.assertEqual(dict([(2, 2)]), getCountedPrimeFactors(4))
        self.assertEqual(dict([(5, 1)]), getCountedPrimeFactors(5))
        self.assertEqual(dict([(2, 1), (3, 1)]), getCountedPrimeFactors(6))
        self.assertEqual(dict([(2, 2), (3, 1)]), getCountedPrimeFactors(12))


