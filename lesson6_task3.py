class Worker:
    def __init__(self, name, surname, posit, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.posit = posit


class Position(Worker):
    def __init__(self, name, surname, posit, wage, bonus):
        super().__init__(name, surname, posit, wage, bonus)
        self.get_full_name = f"Фамилия {surname} \nИмя {name}"
        self.get_total_income = self._income.get('wage') + self._income.get('bonus')


pos = Position("Alex", "Ivanov", "Manager", 27000, 12500)
print(pos.get_full_name, f"\nДоход с учетом премии составляет: {pos.get_total_income}")
