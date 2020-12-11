def my_func():
    w_list = (input("Введите одно слово: ")).title()
    print(w_list)
    return w_list


my_func()


def int_func():
    w_list = ((input("Введите несколько  слово через пробел: ")).title()).split()
    for word in w_list:
        if 192 < ord(word[0]):
            w_list.remove(word)
            print(w_list)
    return w_list


int_func()
