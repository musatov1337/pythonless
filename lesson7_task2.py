class Clothes:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def coat_sq(self):
        return f"Площадь ткани для пальто {self.weight / 6.5 + 0.5}"

    def suit_sq(self):
        return f"Площадь ткани для костюма {2 * self.height + 0.3}"

    @property
    def full_cloth_sq(self):
        return f"Общая площадь ткани равна {round((self.weight / 6.5 + 0.5) + (2 * self.height + 0.3), 2)}"


class Coat(Clothes):
    def __init__(self, height, weight):
        super().__init__(height, weight)
        self.coat_sqr = round(self.weight / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Площадь пальто равна {self.coat_sqr}"


class Suit(Clothes):
    def __init__(self, height, weight):
        super().__init__(height, weight)
        self.suit_sqr = round(2 * self.height + 0.3, 2)

    def __str__(self):
        return f"Площадь костюма равна {self.suit_sqr}"


coat = Coat(2, 2)
suit = Suit(2, 3)
print(coat)
print(suit)
print(coat.full_cloth_sq)
