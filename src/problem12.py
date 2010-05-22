'''
Created on 19/05/2010

@author: Guga

The sequence of triangle numbers is generated by adding the natural numbers.

So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
from functools import reduce
import numbers
import operator
import unittest

def getTriangleNumber(number):
    return sum(range(1, number + 1))

def getDivisorsRecursive(number, set, primeFactors, grouping=None):
    if grouping == None:
        grouping = len(primeFactors)
        
    if grouping <= 1:
        for i in primeFactors:
            set.add(i)
        return
        
    #
    for i in range (0, len(primeFactors) - grouping + 1):
        prod = reduce(operator.mul, primeFactors[i:i + grouping])
        set.add(prod)
    
    getDivisorsRecursive(number, set, primeFactors, grouping - 1)
    
def getDivisors(number):
    divisors = set()
    
    primeFactors = numbers.getPrimeFactors(number)
    
    getDivisorsRecursive(number, divisors, primeFactors)
    
    divisors.add(1)
    return divisors

def answer():
    triangleNumber = 0
    while (True):
        i = 1
        triangleNumber += i 
        divisors = getDivisors(triangleNumber)
        print(triangleNumber, divisors)
        if len(divisors) > 25:
            return triangleNumber
        i += 1

class Test(unittest.TestCase):

    def testGetTriangleNumber(self):
        self.assertEqual(1, getTriangleNumber(1))
        self.assertEqual(3, getTriangleNumber(2))
        self.assertEqual(6, getTriangleNumber(3))
        self.assertEqual(10, getTriangleNumber(4))
        self.assertEqual(15, getTriangleNumber(5))
        self.assertEqual(21, getTriangleNumber(6))
        self.assertEqual(28, getTriangleNumber(7))
        pass
    
    
    def testGetDivisors(self):
        self.assertEqual(set([1, 3]), getDivisors(3))
        self.assertEqual(set([1, 2, 4]), getDivisors(4))
        self.assertEqual(set([1, 2, 3, 6]), getDivisors(6))
        self.assertEqual(set([1, 2, 5, 10]), getDivisors(10))
        self.assertEqual(set([1, 3, 5, 15]), getDivisors(15))
        self.assertEqual(set([1, 2, 4, 5, 10, 20]), getDivisors(20))
        self.assertEqual(set([1, 2, 4, 7, 14, 28]), getDivisors(28))
        


if __name__ == "__main__":
    print(answer())