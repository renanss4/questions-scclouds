from .is_prime import is_prime

def prime_linear(n: int) -> list:
    if n < 2:
        raise ValueError('Input deve ser um número inteiro maior que 1.')
    
    primes = []
    
    if n >= 2:
        primes.append(2)
    
    current = 3
    while current <= n:
        if is_prime(current):
            primes.append(current)
        current += 2  # Pula números pares
    
    return primes