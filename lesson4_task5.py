from functools import reduce


def my_func(f_el, s_el):
    return f_el * s_el


my_list = [el for el in range(99, 1001) if el % 2 == 0]
print(f"Список четных чисел: {my_list}")
print(f"Произведение всех чисел в списке: {(reduce(my_func, my_list))}")
