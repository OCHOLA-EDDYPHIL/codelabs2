def karatsuba(x, y):
    # Base case for recursion.
    if x < 10 or y < 10:
        return x * y

    # Length of the numbers.
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # Split the digits.
    a, b = divmod(x, 10 ** half)
    c, d = divmod(y, 10 ** half)

    # 3 recursive calls.
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Karatsuba's formula.
    return ac * 10 ** (2 * half) + ad_plus_bc * 10 ** half + bd


# Example usage
x = 145623
y = 653324
print("The final product is:", karatsuba(x, y))
