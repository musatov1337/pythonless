class Store:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Устройства': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def check(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Список -\n {self.my_store}')
        except ValueError:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.check(self)


class Printer(Store):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        printer_type = input("Тип принтера: Цветной = Y, Черно-белый = N \n")
        if printer_type == "Y":
            col_type = {'Тип принтера': 'Цветной'}
            self.my_unit.update(col_type)
            if printer_type == "N":
                col_type = {'Тип принтера': 'Черно-белый'}
                self.my_unit.update(col_type)
                return


class Scanner(Store):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        scanner_type = input("Тип сканера: Слайд-сканеры = Y, Проекционные сканеры = N \n")
        if scanner_type == "Y":
            sca_type = {'Тип сканера': 'Слайд-сканеры'}
            self.my_unit.update(sca_type)
            if scanner_type == "N":
                sca_type = {'Тип сканера': 'Проекционные сканеры'}
                self.my_unit.update(sca_type)
                return


class Copier(Store):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        copier_type = input("Тип ксерокса: МФУ = Y, Отдельный ксерокс = N \n")
        if copier_type == "Y":
            cop_type = {'Тип ксерокса': 'МФУ'}
            self.my_unit.update(cop_type)
            if copier_type == "N":
                cop_type = {'Тип ксерокса': 'Отдельный ксерокс'}
                self.my_unit.update(cop_type)
                return


unit_1 = Printer('hp', 2000, 5)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Copier('Xerox', 1500, 1)
print(unit_1.check())
print(unit_2.check())
print(unit_3.check())

