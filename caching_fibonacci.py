def caching_fibonacci():
    # словник для кешування результатів
    cache = {}
    
    def fibonacci(n):
        try:
            # Має бути ціле чмсло
            num = int(n)
            if (num < 0):
                raise ValueError("Число має бути невід'ємним.")
            if (num == 0): return 0
            if (num == 1): return 1
            # Якщо число є в кеші, повертаєм
            if (num in cache):
                print(cache)
                return cache[num]
            # Рекурсія для підрахунків
            cache[num] = fibonacci(n - 1) + fibonacci(n - 2)

            return cache[num]
        except ValueError as err:
             print(f"Помилка: {err}")
        except Exception as err:
            print(f"Сталася помилка: {err}")
        
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
