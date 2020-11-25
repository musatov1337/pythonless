with open("test_2.txt", "r", encoding="utf = 8") as members:
    salary = []
    low_sal = []
    my_list = members.read().split("\n")
    for el in my_list:
        el = el.split()
        salary.append(el[1])
        if int(el[1]) < 20000:
            low_sal.append(el[0])
    print(f"Сотрудники с окладом меньше 20000: {low_sal} \nСредний оклад {(sum(map(int, salary))//len(salary))}")
