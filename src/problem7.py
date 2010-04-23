'''
Created on 10/04/2010

@author: Guga
'''
import problem3
import unittest

if __name__ == '__main__':
    prime = problem3.nextPrime(1)
    for i in range(10001 - 2):
        prime = problem3.nextPrime(prime)    
    print(prime)

class TestProblem7(unittest.TestCase):
    def test(self):
        self.assertEqual(5, problem3.nextPrime(3))
