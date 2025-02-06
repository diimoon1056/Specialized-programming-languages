def reverse_words(sentence):
  words = sentence.split()  # розділяє речення на список слів
  reversed_sentence = ' '.join(reversed(words))  # Реверс список і об'єднання назад у рядок
  return reversed_sentence
  
sentence = input("Введіть речення: ")
print("Реверс слів:", reverse_words(sentence))
