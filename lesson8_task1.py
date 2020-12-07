class Data:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    @classmethod
    def set_data(cls, data):
        day, month, year = data
        return cls(day, month, year)

    @staticmethod
    def valid_data(self):
        if 1 <= self.day <= 31:
            if 1 <= self.month <= 12:
                if 2020 >= self.year >= 0:
                    return f"Дата введена корректно {self.day}.{self.month}.{self.year}!"
                else:
                    return f"Неправильно введен год {self.year}"
            else:
                return f"Неправильно введен месяц {self.month}"
        else:
            return f"неправильно введен день {self.day}"


my_data = [12, 1, 2020]

my_1 = Data.set_data(my_data)
print(my_1.valid_data(my_1))
