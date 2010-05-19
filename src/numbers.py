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

'''
@see: http://en.wikipedia.org/wiki/Power_of_two#Fast_algorithm_to_check_if_a_positive_number_is_a_power_of_two
'''
def isPowerOfTwo(x):
    y = x - 1
    return x & y == 0
    
class Test(unittest.TestCase):
    def testGetDigits(self):
        self.assertEqual([4, 3, 2, 1], getDigits(4321))
