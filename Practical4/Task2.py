class Vector:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

    def __add__(self, other): # додавання двох векторів
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other): #віднімання двох векторів
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented # штука яка перевіряжє щоб клас правильно реагував на ситуації, тобто тип

    def __str__(self):
        return f"({self.x}, {self.y})"

vector1 = Vector(5, 6)
vector2 = Vector(3, 4)

vector_plus = vector1 + vector2
print(f"Сума векторів: {vector_plus}")

vector_minus = vector1 - vector2
print(f"Різниця векторів: {vector_minus}")
