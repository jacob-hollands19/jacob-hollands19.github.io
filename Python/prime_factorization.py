n = int(input("Enter a number: "))

# inorder to find prime factorization we must check primes up till n
# starting at 2 instead of 1 because 1 isnt a real prime
i = 2

factorization = []
# Check that first i * i is not greater than n because if so then we no longer have factors
while i * i <= n:
    # if n is divisible by i then we can find a smaller set of factors thus we add
    # i to the list and take n divided by i
    while (n % i) == 0:
        factorization.append(i)
        n //= i
    # i must now be incremented for the next iteration of the while
    i += 1
# if n is still larger than one its can still have one last factor: itself
if n > 1:
    factorization.append(n)

print(factorization)