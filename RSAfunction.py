from random import randint


def is_prime(n):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    if primo:
        return True
    else:
        return False


def create_h(p, q, phi_n):
    h = 1
    while h < phi_n and is_prime(h):
        h = randint(phi_n - p, phi_n)
    if mcd(h, phi_n) == 1:
        return h


def mcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return mcd(x, y) == 1


def phi_func(n):
    if n == 1:
        return 1
    else:
        n = [y for y in range(1, n) if is_coprime(n, y)]
        return len(n)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


def msg_to_number(text, DIMENSION):
    number = 0
    for i in range(len(text)):
        number += (ord(text[i]) - 96) * pow(DIMENSION, i)
    return number


def number_to_msg(number, DIMENSION):
    text = ""

    cicles = True
    while cicles:
        text += chr(int((number % DIMENSION) + 96))
        number = (number - (number % DIMENSION)) / DIMENSION
        if number == 0:
            cicles = False

    return text
