with open("test_1.txt", "w", encoding="utf = 8") as word:
    word.writelines([f"Hello World\n", "Python is cool\n", "Good bye!\n"])

with open("test_1.txt", "r", encoding="utf = 8") as word:
    content = word.read()
    print(f"Длинна слов в файле {len(content)}")

    word = open("test_1.txt", "r", encoding="utf = 8")
    content = word.readlines()
    print(f"Количество строк: {len(content)}")

    for el in range(len(content)):
        print(f"Номер строки {el + 1} Колличество символов {len(content[el])}")
