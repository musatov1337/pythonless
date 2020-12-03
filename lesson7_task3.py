class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return f"Сложение клеток {self.nucleus + other.nucleus}"

    def __sub__(self, other):
        if (self.nucleus - other.nucleus) < 0:
            return f"Операция неудачна"
        else:
            return f"Вычетание клеток равно {self.nucleus - other.nucleus}"

    def __mul__(self, other):
        return f"Умножение клеток {round(self.nucleus * other.nucleus, 2)}"

    def __truediv__(self, other):
        return f"Делаение клеток {round(self.nucleus / other.nucleus, 2)}"

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.nucleus)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.nucleus % cells_in_row)}'
        return row


cells_1 = Cell(9)
cells_2 = Cell(25)
print(cells_1 + cells_2)
print(cells_1 - cells_2)
print(cells_2.make_order(5))
print(cells_1 / cells_2)