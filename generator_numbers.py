from typing import Callable
import re
# генератор
def generator_numbers(text: str):
    # \b - границя слова, \d+ - одну або більше цифру, \. крапка
    pattern = r'\b\d+\.\d+\b'
    all_numbers = re.findall(pattern, text)
    
    for number in all_numbers:
        # перетворюємо строку в число
        yield float(number)

    
def sum_profit(text: str, func: Callable):
    try:
        #сума знайдених чисел
        res = sum(func(text))
        return res
    except TypeError as err:
        print(f"Помилка типу: {err}")
    
    return 0


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")