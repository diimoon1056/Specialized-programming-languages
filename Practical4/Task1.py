class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # Чисельник
        self.denominator = denominator  # Знаменник
    
    def is_valid(self):
        return 0 < abs(self.numerator) < abs(self.denominator)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


fraction = Fraction(11, 35)
if fraction.is_valid():
    print(f"Дріб {fraction} є правильним.")
else:
    print(f"Дріб {fraction} не є правильним.")
