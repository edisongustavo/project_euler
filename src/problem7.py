'''
Created on 10/04/2010

@author: Guga

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''
import primes
import unittest

def getIthPrime(number):
    primeGenerator = primes.PrimeGenerator()
    for i in range(number):
        prime = primeGenerator.nextPrime()
    return prime

def answer():
    return getIthPrime(10001)

if __name__ == '__main__':
    print((answer()))

class TestProblem7(unittest.TestCase):
    def testIthPrime(self):
        self.assertEqual(13, getIthPrime(6))
        
    def testAnswer(self):
        self.assertEqual(104743, answer())