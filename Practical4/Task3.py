class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name        
        self.age = age          

    def __str__(self):
        return f"{self.name} ({self.species}), Вік: {self.age} рок(и, ів)"


class ZooPark:
    def __init__(self):
        self.animals = []  # Список тварин у зоопарку

    def add_animal(self, animal): # Додавання тварини в зоопарк
        self.animals.append(animal)

    def remove_animal(self, animal): # Видалення тварини із зоопарку
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print(f"Тварина {animal} не знайдена у зоопарку.")

    def show_animals(self):
        if self.animals:
            print("Тварини у зоопарку:")
            for animal in self.animals:
                print(animal)
        else:
            print("У зоопарку немає тварин.")


zoo = ZooPark()

# Створення тварин з параметрами ім'я, вид та вік
kozel = Animal("Козел", "ЯША", age=14)
baran = Animal("Баран", "ШОН", age=6)
pityx = Animal("Пітух", "ПІН", age=2)

# Додавання тварин у зоопарк
zoo.add_animal(kozel)
zoo.add_animal(baran)
zoo.add_animal(pityx)

zoo.show_animals()

zoo.remove_animal(baran)

zoo.show_animals()
