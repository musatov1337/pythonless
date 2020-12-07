class ZeroDiv:
    def __init__(self, divider, dividend):
        self.divider = int(divider)
        self.dividend = int(dividend)

    @staticmethod
    def zero_div(self):
        try:
            self.result = self.divider / self.dividend
        except ZeroDivisionError as err:
            return f"Нельзя делить на ноль {err}"
        else:
            return f"Результат равен: {self.result}"


div = ZeroDiv(10, 0)
print(div.zero_div(div))
