'''
Created on 06/05/2010

@author: emuenz

In the 2020 grid below, four numbers along a diagonal line have been marked in red.
                        begin    end
                        \/       \/
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 <- begin
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 <- end
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26  63  78  14 = 1788696.

What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 2020 grid?
'''
from functools import reduce
import unittest
import operator

numbers = [
[8, 0, 22, 97, 38, 15, 0, 40, 0, 75, 0, 0, 0, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 0, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 0, 49, 13, 36, 65],
[52, 70, 95, 23, 0, 60, 11, 42, 69, 24, 68, 56, 0, 32, 56, 71, 37, 0, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 0, 45, 0, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 0, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 0, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 0, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 0, 80, 0, 62, 16, 14, 0, 53, 56, 92],
[16, 39, 0, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 0, 48, 35, 71, 89, 0, 0, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 0, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 0, 89, 55, 40],
[0, 52, 8, 83, 97, 35, 99, 16, 0, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 0, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[0, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 0, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 0, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 0, 54],
[0, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 0, 89, 19, 67, 48]]

def getListOfNeighbours(i, j, allNumbers, numOfNeighbours):
    allNeighbours = []
    
    def appendWith(fun, listWithAllMembers, matrix, numberOfNeighbours):
            elements = []
            for index in range(0, numberOfNeighbours):
                x, y = fun(index)
                if x >= len(matrix) or y >= len(matrix[0]) or x < 0 or y < 0:
                    return
                elements.append(matrix[x][y])
            listWithAllMembers.append(elements)
    
    appendWith(lambda index: [i         , index + j], allNeighbours, allNumbers, numOfNeighbours) #horizontal
    appendWith(lambda index: [index + i , j        ], allNeighbours, allNumbers, numOfNeighbours) #vertical    
    appendWith(lambda index: [index - i , index + j], allNeighbours, allNumbers, numOfNeighbours) #top-right
    appendWith(lambda index: [index - i , index - j], allNeighbours, allNumbers, numOfNeighbours) #top-left
    appendWith(lambda index: [index + i , index + j], allNeighbours, allNumbers, numOfNeighbours) #bottom-right
    appendWith(lambda index: [index + i , index - j], allNeighbours, allNumbers, numOfNeighbours) #bottom-left

    if not allNeighbours:
        allNeighbours.append([0] * numOfNeighbours)
        
    return allNeighbours

def findHighestProd(matrix, numOfNumbers=4):
    highestProd = 0
    numbers = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            listOfNeighbours = getListOfNeighbours(i, j, matrix, numOfNumbers)
            for neighbours in listOfNeighbours:
                prod = reduce(operator.mul, neighbours)
                if prod > highestProd:
                    numbers = neighbours
                    highestProd = prod
#                    print("Possible highest at: ({0},{1}) = {2}".format(i, j, numbers))
#                    print(listOfNeighbours)

    print(numbers)
    return highestProd

class Test(unittest.TestCase):
    def testHighestOnHorizontal(self):
        nums = [[8 , 2 , 22, 97],
                [49, 49, 99, 40],
                [81, 49, 31, 0],
                [52, 70, 95, 23],
                [10, 70, 0 , 5]]
        self.assertEqual(70 * 95, findHighestProd(nums, 2))
        
    def testHighestOnVertical(self):
        nums = [[8 , 2 , 22, 0],
                [49, 49, 99, 40],
                [81, 49, 31, 73],
                [52, 70, 95, 23],
                [10, 70, 99, 5]]
        self.assertEqual(95 * 99, findHighestProd(nums, 2))
        
    def testHighestOnDiagonal(self):
        nums = [[8 , 2 , 22, 97],
                [49, 49, 99, 40],
                [81, 49, 31, 73],
                [99, 70, 95, 23],
                [0 , 99, 0 , 0]]
        self.assertEqual(99 * 99, findHighestProd(nums, 2))
        
    def testWith3Nums(self):
        nums = [[8 , 2 , 22, 97],
                [49, 49, 99, 40],
                [81, 49, 31, 73],
                [99, 70, 95, 23],
                [0 , 0 , 0 , 0]]
        self.assertEqual(99 * 70 * 95, findHighestProd(nums, 3))

if __name__ == "__main__":
    print(findHighestProd(numbers, 4))
