my_list = list(input("список"))
y = 0

for el in range(int(len(my_list) / 2)):
    my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
    y += 2
print(my_list)
