sumNaturalNumbers.py
------------------------

def sumNatural(num):
    total = 0
    total = num * ( num + 1)
    total = total / 2
    return total


myNum = float(input('enter the natural number'))

if ( myNum > 0 ):
    print('sum of natural number is', sumNatural(myNum) )
else:
    print('please enter natural number')


findNum.py
-----
def positiveNegativeZero(num):
    if( num == 0 ):
        print(num, 'equal to 0')
    elif( num > 0):
        print(num, 'is greater than 0 - positive')
    else:
        print(num, 'less than 0 - negative')


mynum = float(input('please enter the number to check'))
positiveNegativeZero(mynum)


reverseString.py
---------

def reverse(myString):
    newReverseString = ""
    for i in myString:
        print(i)
        newReverseString = i + newReverseString
    return newReverseString

myString = "Hello, there"
reverseString = reverse(myString)
print('reverse string is', reverseString)

stringLen.py
--------
def calLength(mystring):
    total = 0
    for i in mystring:
        total = total + 1
        print(i)
    return total

mystring = "Hello,   there"
len = calLength(mystring)
print('length is', len)


average.py
------

def collectNumbers(totalNum):
    print('please enter', totalNum, 'numbers')
    for i in range(0,totalNum):
        a = float(input())
        myList.append(a)

def calculateAvg():
    total = 0
    for i in range(0,len(myList)):
        total = total + myList[i]
    return(total/totalNum)


myList = []

totalNum = int(input('How many numbers to cal average'))
collectNumbers(totalNum)
avg = calculateAvg()
print('average is', avg)

swapping.py
------------
a = -15
b = -10

a = a + b
b = a - b
a = a - b

print("after swap")
print('a', a)
print('b', b)

