'''
Created on 22/01/2011

@author: emuenz

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
'''
import unittest
import cProfile
import primes
import operator

def isDivisible(number, quocient):
    return number % quocient == 0

def computeSmallestNumberDivisible(top):
    assert(top > 1)
    
    
    nextFactor = reduce(operator.__mul__, primes.PrimeGenerator().primeListUsingSieveOfEratosthenes(top))
    
    i = 0
    while True:
        i = i + 1
        numberToTest = i * nextFactor
        
        found = True
        for x in range(top, 1, -1):
            if not isDivisible(numberToTest, x):
                found = False
                
        if found:
            return numberToTest
                        
class Test(unittest.TestCase):
    def test2(self):
        self.assertEqual(2, computeSmallestNumberDivisible(2))
        
    def test3(self):
        self.assertEqual(6, computeSmallestNumberDivisible(3))
        
    def test4(self):
        self.assertEqual(12, computeSmallestNumberDivisible(4))
        
    def test5(self):
        self.assertEqual(60, computeSmallestNumberDivisible(5))
        
    def test6(self):
        self.assertEqual(60, computeSmallestNumberDivisible(6))
        
    def test2520(self):
        self.assertEqual(2520, computeSmallestNumberDivisible(10))

def answer():
    return computeSmallestNumberDivisible(20)

if __name__ == "__main__":
    cProfile.run('print(answer())')