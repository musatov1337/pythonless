from random import randrange


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} машина поехала со скоростью {self.speed}!"

    def stop(self):
        return f"{self.name} остановился"

    def turn(self):
        num = randrange(0, 3)
        if num == 0:
            return f"{self.name} повернул на лево"
        if num == 1:
            return f"{self.name} повернул на право"
        if num == 2:
            return f"{self.name} повернул назад"

    def show_speed(self):
        return f"Данная скорость автомобиля :{self.name}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed >= 60:
            return f"Машина {self.name} привышает скорость!"
        else:
            return f"Машина {self.name} едет с допустимой скоростью"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed >= 40:
            return f"Машина {self.name} привышает скорость!"
        else:
            return f"Машина {self.name} едет с допустимой скоростью"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


lada_priora = PoliceCar(120, "Blue", "Lada Priora", True)
man_truck = WorkCar(60, "Black", "MAN", False)
lambo = SportCar(230, "Yellow", "Lamborghini", False)
bmw = TownCar(70, "White", "BMW x6", False)
print(man_truck.turn())
print(man_truck.color)
print(man_truck.show_speed())
print(lada_priora.stop())
print(lada_priora.color)
print(lada_priora.is_police)
print(lambo.go())
print(lambo.color)
print(bmw.show_speed())
print(bmw.turn())
