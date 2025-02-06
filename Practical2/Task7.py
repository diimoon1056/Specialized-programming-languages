def dict_to(dictionary):
  return list(dictionary.items())  # wцей метод .items() для отримання списку кортежів

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


tuple_list = dict_to(my_dict) 

print(tuple_list)
