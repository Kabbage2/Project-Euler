import math

y= 600851475143

def is_prime(x):
    prime = True
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            prime = False
            break  
    return prime

for i in range(math.isqrt(y)+1, 2, -1):
    if y % i == 0 and is_prime(i):
        print(i)
        break