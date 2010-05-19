'''
Created on 19/05/2010

@author: Guga
'''
import unittest

def getDigits(number):
    quocient = abs(number) // 10
    remain = abs(number) % 10
    digits = [remain]
    while (quocient > 0):
        remain = quocient % 10
        quocient = quocient // 10
        digits.insert(0, remain)
    return digits

class Test(unittest.TestCase):
    def testGetDigits(self):
        self.assertEqual([4, 3, 2, 1], getDigits(4321))
