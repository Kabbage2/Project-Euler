import math

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return(False)
            break
    return(True)
    
primes = []
y = 2

while len(primes) < 10001:
    if is_prime(y) == True:
        primes.append(y)
    y += 1

print(primes[10000])