from itertools import count
from math import factorial


def fact():
    for num in count(1):
        yield factorial(num)


sec_nd = fact()
x = 0
for i in sec_nd:
    if x < 15:
        print(i)
        x += 1
    else:
        break
