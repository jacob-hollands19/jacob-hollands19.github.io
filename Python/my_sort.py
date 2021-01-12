print("Enter one number at a time then press enter to add the next. type q to stop")
exit = True
inList = []
while exit:
    toAdd = input("Enter next num: ")
    if toAdd == "q":
        exit = False
    else:
        if toAdd.isdigit():
            inList.append(int(toAdd))
        else:
            print("Invalid input try again")

def my_sort(inList):
    # for the length of inList sort that value stored at i
    for i in range(1,len(inList)):
        # save the value at i incase it gets moved
        temp = inList[i]
        # check one before i in the list
        j = i - 1
        # while anything before i is lower than it swap places
        while j >= 0 and temp < inList[j]:
            inList[j+1] = inList[j]
            j -= 1
        # save the value we stored in temp and put it after where the last swap was
        inList[j + 1] = temp
        
my_sort(inList)
print(inList)



