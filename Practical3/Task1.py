distanse = float(input("Введіть відстань у кілометрах: "))
def convert_distance(distanse):
    miles = distanse * 0.62137
    return miles
print("Відстань у милях:", convert_distance(distanse))
