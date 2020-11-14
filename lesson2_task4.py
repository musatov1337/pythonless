#по буквам
s = input("Введите несколько слов: ")
word = []
num = 1

for el in range(s.count('') + 1):
    word = s.split()
    if len(str(s)) <= 10:
        print({f"{num} {s[el]}"})
        num += 1
    else:
        print(f"{num} {s[el][0:10]}")
        num += 1

#по словам

t = input("Введите несколько слов: ").split()
num = 1

for el in t:
    print(f"{num}: {el}")
    num += 1
