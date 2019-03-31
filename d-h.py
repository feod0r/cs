from random import getrandbits
from random import randint

bitDepth = 12


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(module):
    required_set = set(num for num in range(1, module) if gcd(num, module) == 1)
    for g in range(1, module):
        actual_set = set(g**powers % module for powers in range(1, module))
        if required_set == actual_set:
            return g


def get_random_prime():
    while True:
        n = getrandbits(bitDepth) + 3
        if all(n % i for i in range(2, n)):
            return n


# Создание приватных ключей
alice_private = randint(999, 999999)
print('Приватный ключ Алисы', alice_private)
bob_private = randint(999, 999999)
print('Приватный ключ Боба', bob_private)

# Создание простого числа и его первообразного корня по модулю P
p = get_random_prime()
g = primitive_root(p)

print('Простое число: p =', p)
print('Первообразный корень по модулю p: g =', g)

# Создание публичных ключей
alice_public = g**alice_private % p
bob_public = g**bob_private % p

print('Публичный ключ Алисы', alice_public)
print('Публичный ключ Боба', bob_public)

alice_key = (bob_public**alice_private) % p
bob_key = (alice_public**bob_private) % p

print('Секретный ключ(Алиса/Боб):', alice_key, "==", bob_key)
