# we use this to find the numbers with two positive divisors from 1 to 10^9
# if it has two proper divisors, then it is a square of a prime number

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_numbers_with_two_positive_divisors():
    numbers = []
    for i in range(2, 31622): # sqrt(10^9)
        if is_prime(i):
            numbers.append(i * i)
    return numbers

print(find_numbers_with_two_positive_divisors())
