def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# Отримуємо функцію fibonacci з кешуванням
fib = caching_fibonacci()

# Приклад використання
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(20))  # Виведе 6765
print(fib(30))  # Виведе 832040
