import os
from functools import wraps


def log(filename=None, directory="data"):
    """Декоратор, ждя вывода лога выполнения функций в файл (по умолчанию в консоль)
    в директорию (по умолчанию в data"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            message = ""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} is ok."
                return result

            except Exception as e_message:
                message = (
                    f"{func.__name__} error: {e_message.__class__.__name__}: " f"{e_message}. Input: {args}, {kwargs}."
                )
                return e_message

            finally:
                if not filename:
                    print(message)
                else:
                    os.chdir(".")
                    if not os.path.exists(directory):  # создать путь, если не существует
                        os.makedirs(directory)

                    with open(os.path.join(directory, filename), "a", encoding="UTF-8") as file:
                        file.write(f"{message}\n")

        return inner

    return wrapper

