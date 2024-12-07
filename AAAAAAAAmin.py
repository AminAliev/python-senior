class Color:
    def __init__(self, color):
        self.color = color

    def describe_color(self):
        return f"Цвет объекта: {self.color}"


# Родительский класс 2
class Dimensions:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# Родительский класс 3
class Material:
    def __init__(self, material):
        self.material = material

    def describe_material(self):
        return f"Материал объекта: {self.material}"


# Дочерний класс, наследующийся от всех трех
class ComplexObject(Color, Dimensions, Material):
    def __init__(self, color, width, height, material):
        # Инициализация всех родительских классов
        Color.__init__(self, color)
        Dimensions.__init__(self, width, height)
        Material.__init__(self, material)

    def describe_object(self):
        # Комплексное описание объекта
        return (
            f"{self.describe_color()}, "
            f"площадь: {self.calculate_area()} кв. ед., "
            f"материал: {self.describe_material()}."
        )


# Создание экземпляра ComplexObject
obj = ComplexObject("синий", 5, 10, "дерево")

# Использование методов
print(obj.describe_color())       # Цвет объекта: синий
print(obj.calculate_area())       # 50
print(obj.describe_material())    # Материал объекта: дерево
print(obj.describe_object())      # Цвет объекта: синий, площадь: 50 кв. ед., материал: Материал объекта: дерево.
