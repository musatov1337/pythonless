from random import randrange

with open("numbers.txt", "w", encoding="utf = 8") as num:
    for el in range(10):
        numbers = randrange(0, 9)
        num.write(str(numbers) + " ")

with open("numbers.txt", "r", encoding="utf = 8") as s_num:
    my_list = s_num.read().split()
    print(f"Сумма чисел в файле равна: {sum(map(int, my_list))}")
