from .is_prime import is_prime

def prime_recursive(n: int, current: int = 2) -> list:
    if n < 2:
        raise ValueError('Input deve ser um número inteiro maior que 1.')
    
    if current > n:
        return []
    
    if current == 2:
        if n >= 2:
            return [2] + prime_recursive(n, 3)
        else:
            return []
    
    if is_prime(current):
        return [current] + prime_recursive(n, current + 2)
    
    return prime_recursive(n, current + 2)