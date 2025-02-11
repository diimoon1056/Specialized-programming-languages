number = int(input("Введіть число для рахування факторіалу: "))
def factorial_cycle(number):
    result = 1
    for i in range(1, int(number) + 1):
        result *= i
    return result
print(f"Факторіал числа {number} дорівнює {factorial_cycle(number)}")
