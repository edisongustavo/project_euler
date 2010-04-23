'''
Created on 10/04/2010

@author: Guga

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
import unittest

calculatedPrimes = [1, 2]

def isPrime(number):
    if number in calculatedPrimes:
        return True

    lastDigit = number % 10
    if lastDigit in [2, 5] and number not in [2, 5]:
        return False

    i = calculatedPrimes[-1]
    while (i < math.sqrt(number) + 1):
        if number % i == 0:
            return False
        i += 2
        
    calculatedPrimes.append(number)

    return True

def nextPrime (number):
    while (True):
        number += 2
        if isPrime(number):
            return number

    return None
    
def nextPrimeFactor(number, startingFactor=1):
    i = startingFactor
    
    if startingFactor == 2:
        i = 3

    while i < number:
        i = nextPrime(i)

        if number % i == 0:
            return i
        

    return None

def simplifyNumberToCalculate(numToCalculate, fac, total=1):
    while numToCalculate % fac == 0:
        numToCalculate /= fac
        total *= fac
        
    return numToCalculate , total

def getPrimeFactors(num):
    fac = 1
    total = 1.0
    ret = []
    
    numToCalculate = num
    
    if numToCalculate % 2 == 0:
        print("factor = {0}".format(2))
        ret.append(2)
        numToCalculate , total = simplifyNumberToCalculate(numToCalculate, 2, total)
       
    while (fac != None):
        fac = nextPrimeFactor(numToCalculate, fac)
        if fac != None:
            numToCalculate , total = simplifyNumberToCalculate(numToCalculate, fac, total)
            ret.append(fac)
            print("factor = {0}".format(fac))
        if total == num:
            break
    return ret

if __name__ == '__main__':
    for num in getPrimeFactors(600851475143):
        print (num)


class TestProblem3(unittest.TestCase):
    def test(self):
        self.assertEqual([5, 7, 13, 29], getPrimeFactors(13195))

