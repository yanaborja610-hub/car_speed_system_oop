class Car:
    def __init__(self, year_model,make):
        self.__year_model = year_model
        self._make = make
        self.__speed = 0