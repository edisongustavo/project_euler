'''
Created on 03/05/2010

@author: emuenz
'''
import bisect
import math
import unittest

def binary_search(container, value):
    i = bisect.bisect_right(container, value)
    return container[i - 1] == value

class SieveOfEratosthenes():
        def __init__(self):
            pass
            
        def calculate(self, number):
            booleanListOfPrimes = [1] * (int(number) + 1)
            
            lowerBound = 2
            upperBound = lowerBound ** 2
        
            while upperBound <= number:
                for i in range(upperBound, number + 1, lowerBound):
                    booleanListOfPrimes[i] = 0
        
                #find next lower bound
                for i in range(lowerBound + 1, number + 1):
                    if booleanListOfPrimes[i] == 1:
                        lowerBound = i
                        break
                    
                upperBound = lowerBound ** 2
                
            self.booleanListOfPrimes = booleanListOfPrimes
            
        def getList(self):
            return self._createList(self.booleanListOfPrimes)
        
        def _createList(self, booleanListOfPrimes):
            primesList = []
            for i in range(2, booleanListOfPrimes.__len__()):
                if booleanListOfPrimes[i] == 1:
                    primesList.append(i)
            return primesList

class PrimeGenerator:
    
    def __init__(self):
        self._primesCache = []
        self.sieveOfEratosthenesCache = SieveOfEratosthenes()
        
    '''
    http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    
    Calculates a list of primes up to 'number'
    '''
    def primeListUsingSieveOfEratosthenes(self, number):
        #checks if cache contains enough primes
        if len(self._primesCache) > 0 and self._primesCache[-1] >= number:
            i = bisect.bisect_left(self._primesCache, number)
            return self._primesCache[0:i]

        print ("Didnt reach cache on primeListUsingSieveOfEratosthenes for ", number)
        self.sieveOfEratosthenesCache.calculate(number)
        primesList = self.sieveOfEratosthenesCache.getList()
        print ("Finished building prime list")
        
        self._storeInCache(primesList)
        
        return primesList
    
    def _storeInCache(self, prime):
        try:
            if prime.__len__() > self._primesCache.__len__():
                self._primesCache = prime
        except:
            self._primesCache.append(prime)
            
    '''
    Simply loops up to SQRT(number) dividing the number by each prime that was already found
    '''
    def _isPrime_BruteForce(self, number):
        upperBound = math.sqrt(number) + 1
        for i in self._primesCache:
            if number % i == 0:
                return False
            if i > upperBound:
                break;
    
        self._primesCache.append(number)
        return True

    def isPrime(self, number):
        if number < 2:
            return False
    
        if binary_search(self._primesCache, number):
            return True
        
        return self._isPrime_BruteForce(number)

    def nextPrime (self):
        if len(self._primesCache) == 0:
            self._storeInCache(2)
            return 2
        
        number = self._primesCache[-1]
        
        if number == 2:
            self._storeInCache(3)
            return 3
            
        while (True):
            number += 2
            if self.isPrime(number):
                return number
    
        return None

class TestPrimes(unittest.TestCase):
    primesGenerator = PrimeGenerator()
    
    def testNextPrime(self):
        primeGenerator = PrimeGenerator()
        self.assertEqual(2, primeGenerator.nextPrime())
        self.assertEqual(3, primeGenerator.nextPrime())
        self.assertEqual(5, primeGenerator.nextPrime())
        self.assertEqual(7, primeGenerator.nextPrime())
        self.assertEqual(11, primeGenerator.nextPrime())
        
    def testPrimeListUsingSieveOfEratosthenes(self):
        self.assertEqual([2, 3], self.primesGenerator.primeListUsingSieveOfEratosthenes(3))
        self.assertEqual([2, 3], self.primesGenerator.primeListUsingSieveOfEratosthenes(4))
        self.assertEqual([2, 3, 5], self.primesGenerator.primeListUsingSieveOfEratosthenes(5))
        self.assertEqual([2, 3, 5], self.primesGenerator.primeListUsingSieveOfEratosthenes(6))
        self.assertEqual([2, 3, 5, 7], self.primesGenerator.primeListUsingSieveOfEratosthenes(7))
        self.assertEqual([2, 3, 5, 7], self.primesGenerator.primeListUsingSieveOfEratosthenes(10))
