'''
Created on 08/04/2010

@author: emuenz

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the
square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''

if __name__ == '__main__':
    sumOfSquares = 0
    squareOfSum = 0
    for i in range(1, 101):
        sumOfSquares += i ** 2
        squareOfSum += i

    squareOfSum = squareOfSum ** 2
    
    print("{0} - {1}").format(squareOfSum, sumOfSquares)
    print(squareOfSum - sumOfSquares) 
