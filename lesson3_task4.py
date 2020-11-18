def my_func(x, y):
    a = x
    for i in range(y - 1):
        a *= x
    return 1 / a


print(my_func(x=int(input("Введите целое положительное число: ")),
              y=abs(int(input("Введите целое отрицательное число: ")))))


# вторая реализация.
def my_func(x, y):
    a = x
    for i in range(y - 1):
        a *= x
    return 1 / a


print(my_func(x=abs(int(input("Введите целое положительное число: "))),
                    y=abs(int(input("Введите целое отрицательное число: ")))))
