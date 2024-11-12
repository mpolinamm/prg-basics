def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False 
    return True 

N = int(input("Enter the number of leading prime numbers to find: "))

primes = []
num = 2 

while len(primes) < N:
    if is_prime(num):
        primes.append(num)  
    num += 1 

print(f"The first {N} prime numbers are: {primes}")
