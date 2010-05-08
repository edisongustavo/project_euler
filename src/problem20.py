'''
Created on 08/05/2010

@author: Guga

n! means n  (n  1)  ...  3  2  1

Find the sum of the digits in the number 100!
'''
from problem4 import getDigits
import math

if __name__ == '__main__':
    print(sum(getDigits(math.factorial(100))))
