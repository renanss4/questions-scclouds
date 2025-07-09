from fibonacci.fibonacci_linear import fibonacci_linear
from fibonacci.fibonacci_recursive import fibonacci_recursive
from prime.prime_linear import prime_linear
from prime.prime_recursive import prime_recursive

# Testes de Fibonacci
print("=== FIBONACCI ===")
print(f"fibonacci_linear(9): {fibonacci_linear(9)}")  # 34
print(f"fibonacci_recursive(5): {fibonacci_recursive(5)}")  # 5

# Testes de Números Primos
print("\n=== NÚMEROS PRIMOS ===")
test_n = 100

print(f"prime_linear({test_n}): {prime_linear(test_n)}")
print(f"prime_recursive({test_n}): {prime_recursive(test_n)}")