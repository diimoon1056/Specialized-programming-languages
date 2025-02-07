num = float(input("Введіть число: "))
def factorial(num):
  if num == 0 or num == 1:
      return 1
  else:
      return num * factorial(num - 1)
print("Факторіал числа", num, "дорівнює", factorial(num))
