class TriangleException(Exception):
    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message

    def __str__(self):
        return f'Triangle ERROR!\n{self.name}\n{self.message}'

class TriangleExistsError(TriangleException):
    def __init__(self, side: float | int, other_sides: list[int | float]):
        self.side = side
        self.other_sides = tuple(other_sides)
        super().__init__('Ошибка создания',
                         f'Треугольник не может быть создан, так как сторона {side}, '
                         f'больше суммы двух других сторон {other_sides}.')

class TriangleNegativeValueError(TriangleException):
    def __init__(self, side):
        super().__init__('Ошибка данных',
                         f'Сторона треугольника не может иметь отрицательную длину {side}')

class TriangleValueError(TriangleException):
    def __init__(self, side):
        super().__init__('Ошибка данных',
                         f'Сторона треугльника должна быть числом {side}')