'''
Created on 08/04/2010

@author: emuenz

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.
'''

def nextFib(term1, term2):
    return term1 + term2

if __name__ == '__main__':
    sum = 2
    
    previousTerm = 2
    term = nextFib(1, previousTerm)
    
    while term < 4000000:
        if term % 2 == 0:
            sum += term

        nextTerm = nextFib(previousTerm, term)
        previousTerm = term
        term = nextTerm

    print(sum)
