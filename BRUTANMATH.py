import math

def check_integer(value):
    if not isinstance(value, int):
        raise ValueError("Значение не является целым числом")

try:
    first_katet = int(input(" Длина первого катета: "))
    check_integer(first_katet)
except ValueError as e:
    raise ValueError('чел... как же ты слаб в целочисленнии...')

try:
    second_katet = int(input(" Длина первого катета: "))
    check_integer(second_katet)
except ValueError as e:
    raise ValueError('чел... как же ты слаб в целочисленнии...')

gipotenusa = math.sqrt(first_katet**2 + second_katet**2);
perimeter = first_katet + second_katet + gipotenusa;
area = 0.5 * first_katet * second_katet

print("\n Введенные значения:")
print("Длина первого катета:", first_katet)
print("Длина второго катета:", second_katet)

print("\n Результаты:")
print("Длина гипотенузы:", round(gipotenusa, 2))
print("Периметр:", round(perimeter, 2))
print("Площадь:", round(area, 2))