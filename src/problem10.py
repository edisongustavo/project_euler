'''
Created on 03/05/2010

@author: emuenz

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import primes
import cProfile

def getPrimeSumBelow(num):
    if num <= 1:
        return 0
    if num <= 2:
        return 2

    primesList = primes.PrimeGenerator().primeListUsingSieveOfEratosthenes(num)

    return sum(primesList)

if __name__ == "__main__":
    cProfile.run('print(getPrimeSumBelow(2000000))')


def testBelow10():
    assert 2 + 3 + 5 + 7 == getPrimeSumBelow(10)

def testBelow15():
    assert 2 + 3 + 5 + 7 + 11 + 13 == getPrimeSumBelow(15)

def testBelow23():
    assert 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 == getPrimeSumBelow(23)
