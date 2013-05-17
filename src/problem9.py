'''
Created on 22/04/2010

@author: emuenz

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import unittest

def isPythagoreanTriplet(a, b, c):
    return c ** 2 == a ** 2 + b ** 2

def findDaShit(desiredSum):
    i = 0
    a = 0
    
    
    firstTerm = desiredSum / 2
    
    while a < 1000:
        a += 1
        b = a
        while b < 1000:
            b += 1
            i += 1
            
            c = abs(firstTerm - (a * b / desiredSum))
            
            if isPythagoreanTriplet(a, b, c):
                print(("{0} loops".format(i)))
                return a, b, c

if __name__ == "__main__":
    a, b, c = findDaShit(1000)
    print(("a={a}, b={b}, c={c}".format(a=a, b=b, c=c)))
    print(("a*b*c = {0}".format(a * b * c)))

class Test(unittest.TestCase):
    def test345(self):
        self.assertEqual((3, 4, 5), findDaShit(3 + 4 + 5))
    def test1000(self):
        self.assertEqual((200, 375, 425), findDaShit(1000))

