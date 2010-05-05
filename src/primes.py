'''
Created on 03/05/2010

@author: emuenz
'''
from bisect import bisect
import math

calculatedPrimes = [2, 3, 5]

def binary_search(container, value):
    i = bisect(container, value)
    return container[i - 1] == value
    
def isPrime(number):
    if binary_search(calculatedPrimes, number):
        return True

#    lastDigit = number % 10
#    if lastDigit in [2, 5] and number not in [2, 5]:
#        return False

    i = calculatedPrimes[-1]
    upperBound = math.sqrt(number) + 1
    while (i < upperBound):
        if number % i == 0:
            return False
        i += 2
    
    calculatedPrimes.append(i - 2)

    return True

def nextPrime (number):
    while (True):
        number += 2
        if isPrime(number):
            return number

    return None
