'''
Created on 03/05/2010

@author: emuenz

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from primes import nextPrime
import cProfile
import unittest


def getPrimeSumBelow(num):
    sum = 5
    prime = 3
    while True:
        prime = nextPrime(prime)
        if prime > num:
            break

        sum += prime

    return sum

if __name__ == "__main__":
#    cProfile.run('getPrimeSumBelow(2000000)')
    print(getPrimeSumBelow(2000000))
    
class Test(unittest.TestCase):

    def testBelow10(self):
        self.assertEqual(17, getPrimeSumBelow(10))
        
