class FibonacciContainer:
    def __init__(self, n):
        # Генерація перших n чисел Фібоначчі
        self.fibonacci_sequence = [0, 1]  # Початкові два числа Фібоначчі
        for i in range(2, n):
            next_fib = self.fibonacci_sequence[-1] + self.fibonacci_sequence[-2]
            self.fibonacci_sequence.append(next_fib)

    def __len__(self):
        # Повертає довжину списку чисел Фібоначчі
        return len(self.fibonacci_sequence)

    def __getitem__(self, index):
        # Повертає елемент за індексом
        return self.fibonacci_sequence[index]


container = FibonacciContainer(10)

# Виведення довжини контейнера
print(f"Довжина контейнера: {len(container)}")

# Виведення перших 5 чисел Фібоначчі
print("Перші 5 чисел Фібоначчі:")
for i in range(5):
    print(container[i])
