'''
Created on 19/04/2010

@author: emuenz

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import unittest
import numbers

def bruteForce(numberOfDigits):
    foundNumbers = []
    foundPalindrome = 0
    upperLimit = 10 ** numberOfDigits
    bottomLimit = 10 ** (numberOfDigits - 1)
    for left in range(bottomLimit, upperLimit):
        for right in range(bottomLimit, upperLimit):
            mul = left * right
            if mul > foundPalindrome and isPalindrome(mul):
                foundPalindrome = mul
                foundNumbers = [left, right]

    return foundNumbers



def isPalindrome(number):
    digits = numbers.getDigits(number)
    size = len(digits)
    if size % 2 != 0:
        return False
    
    for i in range(0, size // 2):
        if digits[i] != digits[size - i - 1]:
            return False
    return True

if __name__ == '__main__':
    print(bruteForce(3))

class Test(unittest.TestCase):
    def testIsPalindrome(self):
        self.assertTrue(isPalindrome(9009))
        self.assertTrue(isPalindrome(-9009))
        
    def testBruteForceWith2Digits(self):
        self.assertEqual([91, 99], bruteForce(2))
        
    def testBruteForceWith3Digits(self):
        self.assertEqual([913, 993], bruteForce(3))
