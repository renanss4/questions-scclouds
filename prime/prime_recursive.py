from .is_prime import is_prime

def prime_recursive(n: int, current: int = 2) -> list:
    if n < 2:
        raise ValueError('Input deve ser um número inteiro maior que 1.')
    
    if current > n:
        return []
    
    if is_prime(current):
        return [current] + prime_recursive(n, current + 1)
    
    return prime_recursive(n, current + 1)