import cmath # бібліотека для роботи з комплексними числами яка використовується для розв'язання квадратних рівнянь
import math # бібліотека для роботи з математичними функціями яка дозволить використовувати формули для обчислення форми.
print("Завдання 1", "\n")
age = float(input("Введіть свій вік: "))
day_year = 365 
day_live = age * day_year 
print("Ви прожили", day_live, "днів")
print("\n" "Завдання 2", "\n")
mass = int(input("Введіть масу тіла: "))
accel = int(input("Введіть прискорення: "))
streght = mass * accel # Формула для обчислення сили
print("Значення сили дорівнює:", streght)
print("\n" "Завдання 3", "\n")

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))    
c = float(input("Введіть значення c: "))

D = cmath.sqrt(b**2 - 4*a*c)

x1 = (-b + D) / (2*a)
x2 = (-b - D) / (2*a)
print("Значення x1:" , x1, "\n" "Значення x2:" , x2)

print("\n" "Завдання 4", "\n") 
def heron(a, b, c):
  p = (a + b + c)/2
  return math.sqrt(p*(p-a)*(p-b)*(p-c))

def height(lengh, h):
  return 0.5 * lengh * h

def two_party_angl(a, b, angl):
  return 0.5 * a * b * math.sin(math.radians(angl))
  
print( "Виберіть споісб для обчислення площі трикутника:" "\n" "1. По формулі Герона" "\n" "2. За висотою" "\n" "3. За двома сторонами і кутом між ними")
method = int(input("Введіть номер способу за яким хочете обчислити площу трикутника: "))
if method == 1:
  a = float(input("Введіть сторону a: "))
  b = float(input("Введіть сторону b: "))
  c = float(input("Введіть сторону c: "))
  print("Площа трикутника за формулою Герона дорівнює: ", heron(a, b, c))
elif method == 2:
  lengh = float(input("Введіть довжину трикутника: "))
  h = float(input("Введіть висоту трикутника: "))
  print("Площа трикутника за висотою дорівнює:", height(lengh, h))
elif method == 3:
  a = float(input("Введіть сторону a: "))
  b = float(input("Введіть сторону b: "))
  angl = float(input("Введіть кут між сторонами: "))
  print("Площа трикутника за двома сторонами і кутом між ними дорівнює:", two_party_angl(a, b, angl))
else:
  print("Ви вибрали неправильний номер.")
print("\n" "Завдання 5", "\n")
num_1 = float(input("Введіть перше число: "))
num_2 = float(input("Введіть друге число: "))
num_3 = float(input("Введіть третє число: "))

min = min(num_1, num_2, num_3)
max = max(num_1, num_2, num_3)
print(f"Найменше число: {min} \n Найбільше число: {max}")
print("\n" "Завдання 6" "\n")
N = int(input("Введуть натуральне число від 1 до 100: "))
if 1 <= N <= 100:
  sum = N * (N + 1) / 2
  print(f"Сума перших {N} натуральних чисел дорівнює {sum}")
else:
  while not (1 <= N <= 100):
    N = int(input("Число не входить в діапазон, повторіть спробу: "))
    sum = N * (N + 1) / 2
    print(f"Сума перших {N} натуральних чисел дорівнює {sum}")
print("\n" "Завдання 7", "\n")
num_start = int(input("Введіть початок діапазону: "))
num_end = int(input("Введіть кінець діапазону: "))
for number in range(num_start, num_end + 1):
  if number > 1:
    for i in range(2, number):
      if number % i == 0:
        break
    else:
       print(number)
print("\n" "Завдання 8", "\n")
num = int(input("Введіть ціле число: "))
while num >2:
  num -= 1
  for i in range(2, num):
    if num % i == 0:
      break
  else:
     print(f"Перше просте число яке передує, є: {num}")
