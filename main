import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # выполняем функцию
        end = time.time()
        print(f"⏱ Функция '{func.__name__}' отработала за {end - start:.4f} сек.")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    return "Готово!"


print(slow_function())