'''
Created on 10/04/2010

@author: Guga

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
import primes
import unittest
import numbers
'''
Cant get the prime factors using sieveOfErasthotenes, because the numbers is too big
'''
def calculatePrimeFactorsNaively(number):
    primeFactors = []
    
    #the argument 'number' is too big, so calculate the factors differently
    prime = 1
    upperbound = math.sqrt(number)
    while prime < upperbound:
        prime = primes.nextPrime(prime)
        if number % prime == 0:
            primeFactors.append(prime)
            number = numbers.simplifyNumber(number, prime)
            
    return primeFactors
            
def answer():
    return max(calculatePrimeFactorsNaively(600851475143))
    
if __name__ == '__main__':
    print(answer())

class TestProblem3(unittest.TestCase):
    def test(self):
        self.assertEqual([5, 7, 13, 29], calculatePrimeFactorsNaively(13195))
        
    def testAnswer(self):
        self.assertEqual(6857, answer())

