import math
# pip install typeguard mypy
from typeguard import check_argument_types, check_return_type
# from typing import List

# 1
def sum_multiple_3_5() -> int:
    sum = 0
    for i in range(3,1000+1):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum;

#print(sum_multiple_3_5())


# 2
def even_fibonacci(first: int = 1, second:int = 2) -> int:
    assert check_argument_types()
    a = first
    b = second
    sum = 0
    while (b < 4_000_000):
        c = a + b
        a = b
        b = c 
        if (a % 2 == 0):
            sum += a 
    
    assert check_return_type(sum)
    return sum;

check_argument_types()
print(even_fibonacci())

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

# 4 

def is_palindrome(nb):
    strNb = str(nb)
    start = 0
    end = len(strNb) - 1
    while (start < end):
        if (strNb[start] != strNb[end]):
            return False
        start += 1
        end -= 1
    return True

def largest_palindrome_prod(startProd = 700):
    largest_palindrom_prod = 9009
    for i in range(startProd, 999):
        for j in range(startProd, 999):
            prod = i * j 
            if (prod > largest_palindrom_prod and is_palindrome(prod)):
                largest_palindrom_prod = prod
    return largest_palindrom_prod

#print(largest_palindrome_prod())

# 5

def is_divideable_by_all(nb, limit = 20):
    for divider in range(2,limit + 1):
        if (nb % divider != 0):
            return False
    return True
    

def smallest_multiple():
    max =  1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
    for nb in range(20, max + 1, 20):
        if (is_divideable_by_all(nb)):
            return nb

#print(smallest_multiple())

# 6