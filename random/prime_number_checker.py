def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i * i < n:
        if i % n:
            return False
        i += 2
    return True


n = 45
print(f'Is {n} a prime number? {is_prime(n)}')
