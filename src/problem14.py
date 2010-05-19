'''
Created on 19/05/2010

@author: Guga

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import unittest
import math
import numbers
import cProfile

sequenceCache = dict()

def applySequence(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1
    
def numberOfStepsOfSequence(startingNumber):
    if startingNumber == 1:
        return 0

    if startingNumber in sequenceCache:
        return sequenceCache[startingNumber]
    
# this optimization actually make it slower :P
#    if numbers.isPowerOfTwo(startingNumber):
#        numSteps = math.log(startingNumber) / math.log(2)
#        sequenceCache[startingNumber] = numSteps
#        return numSteps
    
    numSteps = 1 + numberOfStepsOfSequence(applySequence(startingNumber))
    
    sequenceCache[startingNumber] = numSteps
    
    return numSteps

def findLongestChainUnder(number):
    longestChain = 1
    ret = 1
    for i in range(1, number):
        numSteps = numberOfStepsOfSequence(i)
        if numSteps > longestChain:
            ret = i
            longestChain = numSteps
            
    return ret
    
class Test(unittest.TestCase):
    def testCountNumberSteps(self):
        self.assertEqual(9, numberOfStepsOfSequence(13))
        pass
    
    def testCountNumberStepsOfEvenNumbers(self):
        self.assertEqual(4, numberOfStepsOfSequence(16))
        self.assertEqual(3, numberOfStepsOfSequence(8))
        self.assertEqual(2, numberOfStepsOfSequence(4))
        self.assertEqual(1, numberOfStepsOfSequence(2))
        pass
    
    def testFindLongestChainUpTo(self):
        self.assertEqual(9, findLongestChainUnder(14))
        
        numberOfStepsOfSequence(13)

if __name__ == "__main__":
    cProfile.run('print(findLongestChainUnder(1000000))')
