import math

print("Let's see if you know your prime numbers")
print("Go ahead and type one:>")
x = int(input())
for i in range(2, int(math.sqrt(x))+ 1):
    if x % i == 0 and x < 2:
        print("Not a prime number")
    else:
        print("It's a prime number")
