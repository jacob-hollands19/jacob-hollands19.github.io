num = int(input("Enter a number: "))
primeList = []
primeornot = True
if num <= 1:
    print("No Prime Numbers")
    # check all numbers between 2 and num to see if any are prime
    # if num is divisible by any of them, then it is not prime
j = 2
while j <= num:
    primeornot = True
    testNum = j
    for i in range(2, testNum):
        if (testNum % i) == 0:
            primeornot = False
    if primeornot:
        primeList.append(testNum)
    j +=1
print(primeList)    
input()