from itertools import cycle, count


def my_func():
    c = 0
    for word in cycle("АБВ"):
        if c > 7:
            return word
        else:
            for el in count(1):
                if el > 3:
                    break
                else:
                    print(el, word)
                    c += 1
    return my_func()


my_func()
