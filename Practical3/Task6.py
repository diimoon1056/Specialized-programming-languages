sentenсe = input("Введіть речення для пошуку найдовшого слова: ")
def sentenсe_func(sentenсe):
  words = sentenсe.split()
  long_word = max(words, key=len)
  return long_word
print("Найдовше слово у реченні:", sentenсe_func(sentenсe))
