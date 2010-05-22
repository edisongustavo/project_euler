'''
Created on 03/05/2010

@author: emuenz
'''
from bisect import bisect
import array
import math
import unittest

calculatedPrimes = [2, 3, 5]

def binary_search(container, value):
    i = bisect(container, value)
    return container[i - 1] == value

'''
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Calculates a list of prime numbers up to 'number'
'''
def primeListUsingSieveOfEratosthenes(number):
    booleanListOfPrimes = array.array('b', [1] * (number + 1))

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

    return createList(booleanListOfPrimes)

def createList(booleanListOfPrimes):
    primesList = []
    for i in range(2, booleanListOfPrimes.__len__()):
        if booleanListOfPrimes[i] == 1:
            primesList.append(i)
    return primesList
    
'''
Simply loops up to SQRT(number) dividing the number by each prime that was already found
'''
def isPrime_BruteForce(number):
    upperBound = math.sqrt(number) + 1
    for i in calculatedPrimes:
        if number % i == 0:
            return False
        if i > upperBound:
            break;

    calculatedPrimes.append(number)
    return True

def isPrime(number):
    if number < 2:
        return False

    if binary_search(calculatedPrimes, number):
        return True
    
    return isPrime_BruteForce(number)

def nextPrime (number):
    if number == 1:
        return 2
    if number == 2:
        return 3
    
    if number % 2 == 0:
        number -= 1

    while (True):
        number += 2
        if isPrime(number):
            return number

    return None


class Test(unittest.TestCase):

    def testPrimeListUsingSieveOfEratosthenes(self):
        self.assertEqual([2, 3], primeListUsingSieveOfEratosthenes(3))
        self.assertEqual([2, 3], primeListUsingSieveOfEratosthenes(4))
        self.assertEqual([2, 3, 5], primeListUsingSieveOfEratosthenes(5))
        self.assertEqual([2, 3, 5], primeListUsingSieveOfEratosthenes(6))
        self.assertEqual([2, 3, 5, 7], primeListUsingSieveOfEratosthenes(7))
        self.assertEqual([2, 3, 5, 7], primeListUsingSieveOfEratosthenes(10))