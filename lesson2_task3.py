m = int(input("Введите месяц в виде числа"))
year_dict = {"Зима": (1, 2, 12), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}

for key in year_dict.keys():
    if m in year_dict[key]:
        print(f"Время года:  {key}")

year_list = ["Зима", "Весна", "Лето", "Осень"]

n = int(input("Введите месяц в виде числа"))
if n == 1 or n == 2 or n == 12:
    print(f"Время года: {year_list[0]}")
elif n == 3 or n == 4 or n == 5:
    print(f"Время года: {year_list[1]}")
elif n == 6 or n == 7 or n == 8:
    print(f"Время года: {year_list[2]}")
elif n == 9 or n == 10 or n == 11:
    print(f"Время года: {year_list[3]}")
else:
    print("Такого месяца нет.")
