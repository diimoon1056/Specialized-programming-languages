def count_chars(c):
  char_count = {} 
  for char in c:
      char_count[char] = char_count.get(char, 0) + 1  # підраховування входження символів

  return char_count

word= input("Введіть рядок: ")

unique_chars = count_chars(word)

for char, count in unique_chars.items():
  print(f"Символ: '{char}' → {count} раз(и, зів)")
