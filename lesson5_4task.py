with open("test_3.txt", "r", encoding="utf=8") as my_list:
    content = my_list.readlines()
    ru_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_list = []
    for el in content:
        el = el.split()
        new_list.append(ru_dic[el[0]] + ' - ' + el[2] + "\n")
        print(new_list)

with open("new_test.txt","w", encoding="utf=8") as new:
    new.writelines(new_list)





