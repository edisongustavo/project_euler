'''
Created on 10/04/2010

@author: Guga

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''
import primes
import unittest

def answer():
    prime = primes.nextPrime(1)
    for i in range(10001 - 1):
        prime = primes.nextPrime(prime)
    return prime

if __name__ == '__main__':
    print(answer())

class TestProblem7(unittest.TestCase):
    def test(self):
        self.assertEqual(5, primes.nextPrime(3))
    def testAnswer(self):
        self.assertEqual(104743, answer())