result = []

def divider(a, b):
    if a < b:
        raise ValueError("a меньше, чем b")
    if b > 100:
        raise IndexError("b больше 100")
    return a / b

# Корректный словарь данных
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        # Пытаемся выполнить деление
        res = divider(int(key), data[key])  # Приводим ключ к int, если он строка
        result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка деления на ноль: key={key}, value={data[key]}")
    except TypeError:
        print(f"Некорректный тип данных: key={key}, value={data[key]}")
    except ValueError as ve:
        print(f"ValueError: {ve} (key={key}, value={data[key]})")
    except IndexError as ie:
        print(f"IndexError: {ie} (key={key}, value={data[key]})")
    except Exception as e:
        print(f"Непредвиденная ошибка: {type(e).__name__}: {e} (key={key}, value={data[key]})")

print("Результат:", result)
