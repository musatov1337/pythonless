try:
    with open("test_1.txt", "w", encoding="utf-8") as exple:
        print("Введите пробел для завершения.")
        num = 1
        while True:
            line = input(f'Введите {num} элемент в файл: ')
            exple.writelines(f"{line}\n")
            num += 1
            if line == " ":
                break
except IOError:
    print("Ошибка ввода!")
