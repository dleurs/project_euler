import math

# 1
def sum_multiple_3_5():
    sum = 0
    for i in range(3,1000+1):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum;

#print(sum_multiple_3_5())


# 2
def even_fibonacci(first = 1, second = 2):
    a = first
    b = second
    sum = 0
    while (b < 4_000_000):
        c = a + b
        a = b
        b = c 
        if (a % 2 == 0):
            sum += a 
    return sum;

#print(even_fibonacci())

# 3
def prime_factors(nb):
    prime_factors = []
    if (nb % 2 == 0):
        prime_factors.append(2)
    for i in range(3, int(math.sqrt(nb)) + 1, 2):
        if (nb % i == 0):
            if (is_prime(i)):
                prime_factors.append(i)
    return prime_factors

def is_prime(nb):
    if (nb <= 1):
        return False
    if (nb == 2 or nb == 3 or nb == 5 or nb == 7):
        return True
    if (nb % 2 == 0 or nb % 3 == 0 or nb % 5 == 0 or nb % 7 == 0):
        return False
    for i in range (11, int(math.sqrt(nb)) + 1, 2):
        if (nb % i == 0):
            return False  
    return True

#print(prime_factors(600851475143)[-1])
