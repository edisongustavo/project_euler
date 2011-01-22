'''
Created on 22/01/2011

@author: emuenz

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.
'''
import unittest

units = ["one","two","three","four","five","six","seven","eight","nine"]
irregularNumbers = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
roundedDozens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def countLetters(letters):
    return len(letters) - letters.count(" ")

def describe(number):
    desc = ""
    
    #HACK! :D
    if number == 1000:
        return "one thousand"
    
    hundredUnit = number / 100
    number = number % 100
    
    dozenUnit = number / 10
    unit = number % 10
    
    if hundredUnit > 0:
        desc += units[hundredUnit-1] + " hundred"
        if dozenUnit > 0 or unit > 0:
            desc += " and"
    
    if dozenUnit > 0:
        if dozenUnit == 1:
            desc += " " + irregularNumbers[unit]
        else:
            desc += " " + roundedDozens[dozenUnit-2]
            
    if unit > 0 and dozenUnit != 1:
        desc += " " + units[unit-1]
            
    return desc.strip()

def answer():
    size = 0
    
    for i in range(1, 1001):
        size += countLetters(describe(i))
    
    return size

class Test(unittest.TestCase):
    def testZero(self):
        self.assertEqual("", describe(0))
    def testOne(self):
        self.assertEqual("one", describe(1))
    def testTwo(self):
        self.assertEqual("two", describe(2))

    def testTen(self):
        self.assertEqual("ten", describe(10))
    def testEleven(self):
        self.assertEqual("eleven", describe(11))
    def testTwenty(self):
        self.assertEqual("twenty", describe(20))
    def testTwentyOne(self):
        self.assertEqual("twenty one", describe(21))
    def testFourtyTwo(self):
        self.assertEqual("forty two", describe(42))
        
    def testOneHundred(self):
        self.assertEqual("one hundred", describe(100))
    def testOneHundredOne(self):
        self.assertEqual("one hundred and one", describe(101))
    def testOneHundredTwelve(self):
        self.assertEqual("one hundred and twelve", describe(112))
    def testOneHundredFiftySix(self):
        self.assertEqual("one hundred and fifty six", describe(156))
    def testThreeHundredFourtyTwo(self):
        self.assertEqual("three hundred and forty two", describe(342))
        
    def testNineHundredNineteen(self):
        self.assertEqual("nine hundred and nineteen", describe(919))
    def testNineHundredNinetyNine(self):
        self.assertEqual("nine hundred and ninety nine", describe(999))
        
    def testOneThousand(self):
        self.assertEqual("one thousand", describe(1000))

if __name__ == "__main__":
    print(answer())
