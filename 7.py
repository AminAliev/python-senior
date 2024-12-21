class GeneratorIterable:
    def __init__(self, n):
        self.n = n  # количество раз, сколько будет возвращать генератор

    def __iter__(self):
        # Генератор, который будет возвращать числа от 0 до n
        for i in range(self.n):
            yield self._generator_function(i)

    def _generator_function(self, i):
        # Возвращаем генератор, который возвращает квадраты чисел
        for j in range(i, i + 3):
            yield j ** 2


# Пример использования:
gen_iterable = GeneratorIterable(5)
for gen in gen_iterable:
    for value in gen:
        print(value)
