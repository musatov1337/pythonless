def my_func():
    sum_res = 0
    close = False
    while close == False:
        number = (input("ВВедите строку чисел через пробел")).split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                print(f"Финальная сумма: {sum_res}")
                close = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Сумма в данный момент: {res}")


my_func()
