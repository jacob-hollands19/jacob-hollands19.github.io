str1 = input("Enter a string to unscramble: ")
str1 = str1.lower()
f = open("C:\\Users\Jacob\Desktop\Bootcamp\jacob-hollands19.github.io\Python\wordlist.txt", "r")
print(set(str1))
for x in f:
    x = x.strip()
    if len(str1) == len(x) and set(str1) == set(x):
        print(x)
input()