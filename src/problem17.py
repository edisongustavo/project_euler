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
units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
irregularNumbers = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
roundedDozens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def countLetters(letters):
    return len(letters) - letters.count(" ")

def describe(number):
    desc = ""

    # HACK! :D
    if number == 1000:
        return "one thousand"

    hundredUnit = int(number / 100)
    number = number % 100

    dozenUnit = int(number / 10)
    unit = number % 10

    if hundredUnit > 0:
        desc += units[hundredUnit - 1] + " hundred"
        if dozenUnit > 0 or unit > 0:
            desc += " and"

    if dozenUnit > 0:
        if dozenUnit == 1:
            desc += " " + irregularNumbers[unit]
        else:
            desc += " " + roundedDozens[dozenUnit - 2]

    if unit > 0 and dozenUnit != 1:
        desc += " " + units[unit - 1]

    return desc.strip()

def answer():
    size = 0

    for i in range(1, 1001):
        size += countLetters(describe(i))

    return size

def testZero():
    assert "" == describe(0)
def testOne():
    assert "one" == describe(1)
def testTwo():
    assert "two" == describe(2)

def testTen():
    assert "ten" == describe(10)
def testEleven():
    assert "eleven" == describe(11)
def testTwenty():
    assert "twenty" == describe(20)
def testTwentyOne():
    assert "twenty one" == describe(21)
def testFourtyTwo():
    assert "forty two" == describe(42)

def testOneHundred():
    assert "one hundred" == describe(100)
def testOneHundredOne():
    assert "one hundred and one" == describe(101)
def testOneHundredTwelve():
    assert "one hundred and twelve" == describe(112)
def testOneHundredFiftySix():
    assert "one hundred and fifty six" == describe(156)
def testThreeHundredFourtyTwo():
    assert "three hundred and forty two" == describe(342)

def testNineHundredNineteen():
    assert "nine hundred and nineteen" == describe(919)
def testNineHundredNinetyNine():
    assert "nine hundred and ninety nine" == describe(999)

def testOneThousand():
    assert "one thousand" == describe(1000)

if __name__ == "__main__":
    print(answer())
