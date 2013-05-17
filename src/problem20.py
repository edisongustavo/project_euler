'''
Created on 08/05/2010

@author: Guga

n! means n  (n  1)  ...  3  2  1

Find the sum of the digits in the number 100!
'''
import math
import numbers

if __name__ == '__main__':
    print((sum(numbers.getDigits(math.factorial(100)))))
