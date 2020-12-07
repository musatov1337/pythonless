class Exce:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                list_on = int(input("Введите значение: "))
                self.my_list.append(list_on)
                print(f"{self.my_list}")
            except ValueError:
                print(f"Недопустимое значение строка или булево")
                list_in = input("Если не хотите продолжать вводить значения введите 's': ")
                if list_in != "s":
                    print(try_exc.my_input())
                elif list_in == "s" or list_in != "S":
                    return f"Список {self.my_list}"


try_exc = Exce()
print(try_exc.my_input())
