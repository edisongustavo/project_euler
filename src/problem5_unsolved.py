'''
Created on 08/04/2010

@author: emuenz

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
'''

def isDivisible(number, quocient):
    return number % quocient == 0

if __name__ == '__main__':
    
    foundANumber = False
    
    thenumber = 10000000
    aNumber = 0
    while aNumber < thenumber:
        aNumber += 1
        allNumberInSetCanDivide = True
        for i in range(1, 20):
            if not isDivisible(aNumber, i):
                allNumberInSetCanDivide = False
                break
        if allNumberInSetCanDivide and aNumber < thenumber:
            thenumber = aNumber
            foundANumber = True
            break
            
    print thenumber  
