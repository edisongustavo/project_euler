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

'''
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

'''
def primeListUsingSieveOfEratosthenes(number):
    #assume that the number hasn't been calculated
    listOfPrimes = [1] * (number + 1)
    
    lowerBound = 2
    upperBound = lowerBound ** 2

    while upperBound < number:
        for i in range(upperBound, number):
            if i % lowerBound == 0:
                listOfPrimes[i] = 0
        
        #find next lower bound
        for i in range(lowerBound + 1, number):
            if listOfPrimes[i - 1] == 1:
                lowerBound = i
                break
            
        upperBound = lowerBound ** 2

    return createList(listOfPrimes)

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
    if number % 2 == 0:
        number -= 1

    while (True):
        number += 2
        if isPrime(number):
            return number

    return None
