def my_func(a, b, c):
    if a + b > b + c and a + b > a + c:
        return a + b
    if a + b < b + c and a + b < c + a:
        return b + c
    else:
        return a + c


print(my_func(a=int(input("Введите первое число: ")), b=int(input("Введите второе число: ")),
              c=int(input("Введите третье число: "))))
