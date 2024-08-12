def fibonacci_linear(n: int) -> int:
    if n < 0:
        raise ValueError('Input deve ser um número inteiro positivo.')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    x, y = 0, 1
    current_position = 1
    while current_position < n:
        next = x + y
        x = y
        y = next
        current_position += 1
    return y