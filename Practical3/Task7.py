count_words = input("Введіть речення для підрахунку кількості слів: ")
def count_words_func(count_words):
  words = count_words.split()
  count = len(words)
  return count
print("Кількість слів у реченні:", count_words_func(count_words))
