from sys import argv

name, time, payp_hour, bonus = argv


def salary(time, payp_hour, bonus):
    res = (time * payp_hour) + bonus
    month_res = res*21
    return f"Заработная плата сотрудника в день: {res} рублей.\nЗарботная плата в месяц составляет: {month_res} рублей "

print(f"Рабочий день состовляет {time} ч.")
print(f"Оплата в час состовляет {payp_hour} руб.")
print(f"Премия в размере {bonus} руб.")
print(salary(time=int(time), payp_hour=int(payp_hour), bonus=int(bonus)))
