def palindrome(s):
  s = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")  #код який прибирає пробіли та розділові знаки
  return s == s[::-1] #перевірка на паліндром

text = input("Введіть рядок: ")
if palindrome(text):
  print("Це паліндром!")
else:
  print("Це не паліндром.")
