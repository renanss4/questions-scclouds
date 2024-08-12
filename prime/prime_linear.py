from .is_prime import is_prime

def prime_linear(n: int) -> list:
    if n < 2:
        raise ValueError('Input deve ser um número inteiro maior que 1.')
    
    primes = []
    current = 2
    while current <= n:
        if is_prime(current):
            primes.append(current)
        current += 1

    return primes