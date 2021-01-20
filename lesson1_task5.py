proceeds = int(input("Введите размер выручки: "))
cost = int(input("Введитe размер издержек: "))
profit = int(proceeds - cost)

if proceeds > cost:
     rent = profit / proceeds
     members = int(input("Введите численость сотрудников: "))
     profit_mem = profit / members
     print(f"Фирма отработала с прибылью и ее рентабильность составила: {rent}.", f" Размер выручки на одного сотрудника составил: {profit_mem:.2f}")
elif proceeds < cost:
     print("Фирма получила убыток.")
elif proceeds == cost:
    print("Фирма не получила убыток, но и не смогла заработать.")
