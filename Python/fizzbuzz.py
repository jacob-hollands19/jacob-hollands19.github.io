i = 0
while i <= 100:
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))
    i += 1
input()