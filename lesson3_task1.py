def my_func(var_1, var_2):
    try:
        var_1 / var_2
    except ZeroDivisionError:
        print("Ввели неверное число!")
    return var_1 / var_2


print(my_func(var_1=int(input("Введите число")), var_2=int(input("Введите второе число"))))
