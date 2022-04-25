from cmath import sqrt


from math import sqrt


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(round(sqrt(num)))+1):
        if num % i == 0:
            return False
    return True


def sum_primes(num):
    sum = 0
    for i in range(num+1):
        if is_prime(i):
            sum += i
    return sum


print(sum_primes(977))
