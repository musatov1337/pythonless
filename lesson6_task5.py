class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Метод отрисовки {self.draw}")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "\033[2m\033[37m\033[40m {}".format(f"Вы взяли {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "\033[3m\033[34m\033[40m {}".format(f"Вы взяли {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "\033[1m\033[4m\033[37m\033[40m {}".format(f"Вы взяли {self.title}")


pen = Pen("Карандаш")
pencil = Pencil("Ручку")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
