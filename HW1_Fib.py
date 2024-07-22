def caching_fibonacci():
    cache = {}  # Сторення порожнього словника для кешу

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        # Обчислюємо значення рекурсивно та зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Використання:
fib = caching_fibonacci()

# Приклади
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610