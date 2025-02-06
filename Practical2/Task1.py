def average_non(numbers):
  non_negative_numbers = []
  for num in numbers:
      if num >= 0:
          non_negative_numbers.append(num)  # тут додається невід’ємне число до списку
  if not non_negative_numbers:
      return "У списку немає невід’ємних чисел."
  return sum(non_negative_numbers) / len(non_negative_numbers)  # середнє арифметичне
numbers = [-10, 24, 9, 0, -8, -7, -1, 10]
result = average_non(numbers)

print("Середнє арифметичне невід’ємних чисел:", result)
