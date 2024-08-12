def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError('Input deve ser um número inteiro positivo.')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)