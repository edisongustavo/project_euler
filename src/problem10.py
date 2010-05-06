'''
Created on 03/05/2010

@author: emuenz

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from primes import nextPrime, primeListUsingSieveOfEratosthenes
import cProfile
import unittest
import math

def getPrimeSumBelow(num):
    if num <= 1:
        return 0
    if num <= 2:
        return 2
    
    primes = primeListUsingSieveOfEratosthenes(num)
    
    return sum(primes)


import math
 
def doItDiff():
    maxPrime = 2000000
    primeRange = range(3, maxPrime, 2)
    primes = [2]
    stop = 0
     
    while True:
        for i in primeRange:
            if i != -1:
                primes.append(i)
                multToRem = i
                break
        for i in range(0, len(primeRange)):
            if primeRange[i] == multToRem:
                start = i
                break
        for i in range(start, len(primeRange), multToRem):
            primeRange[i] = -1
        stop += 1
        if stop >= maxPrime ** 0.5:
            break
     
    for i in primeRange:
        if i != -1:
            primes.append(i)
     
    print(primes)
    sum = 0
    for i in primes:
        sum += i
     
    print(sum)
 
if __name__ == "__main__":
    cProfile.run('doItDiff()')
#    cProfile.run('doItDifferently(10)')
#    cProfile.run('print (getPrimeSumBelow(2000000))')
#    print(getPrimeSumBelow(2000000))
#    cProfile.run('doItDifferently()')   

    
class Test(unittest.TestCase):

    def testBelow10(self):
        self.assertEqual(2 + 3 + 5 + 7, getPrimeSumBelow(10))
        
    def testBelow15(self):
        self.assertEqual(2 + 3 + 5 + 7 + 11 + 13, getPrimeSumBelow(15))
        
    def testBelow23(self):
        self.assertEqual(2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23, getPrimeSumBelow(23))
