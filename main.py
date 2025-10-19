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

def ana(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    else:
        for i in list(a):
            if i not in b:
                return False

        return True


def anl(a: str):
    v = {}

    for word in a.split():
        v[word] = v.get(word, 0) + 1
    return max(v, key=v.get)


def uniq(a: str):
    words = a.split()
    for word in words:
        if words.count(word) == 1:
            return word
    return None
