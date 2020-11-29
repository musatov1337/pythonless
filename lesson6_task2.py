class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._mass = 25
        self._depth = 5

    def mass(self):
        return round((self._length * self._width * self._mass * self._depth)/1000)


road = Road(5000, 20)
print(road.mass())
