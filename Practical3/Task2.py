num1 = int(input("Введіть число для піднесення до степеня: "))
num2 = int(input("Введіть степінь: "))
def power_number(num1, num2):
    result = 1
    if num2 < 0:
        num1 =1 / num1
        num2 = -num2
    for i in range(int(num2)):
            result *= num1
    return result
        
print(f"{num1} в степені {num2} дорівнює {power_number(num1, num2)}")
