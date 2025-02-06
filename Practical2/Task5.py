matrix = [
  [10, 4, 5],
  [3, 15, 9],
  [6, 7, 1]
]

elements = [(matrix[i][j], i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))] # перетворення матриці в список кортежів (значення, рядок, стовпець)

min_element = min(elements)
max_element = max(elements)

print(f"Мінімальний елемент {min_element[0]} знаходиться у рядку {min_element[1]}, стовпці {min_element[2]}")
print(f"Максимальний елемент {max_element[0]} знаходиться у рядку {max_element[1]}, стовпці {max_element[2]}")
