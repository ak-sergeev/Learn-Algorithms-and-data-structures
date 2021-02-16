def gcd_iter(a, b):
    # Итеративный вариант.
    while b:
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    # Рекурсивный вариант.
    if b:
        return gcd_rec(b, a % b)
    return a
