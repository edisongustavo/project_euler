'''
Created on 08/05/2010

@author: Guga

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
from problem4 import getDigits

if __name__ == '__main__':
    print(sum(getDigits(2 ** 1000)))
