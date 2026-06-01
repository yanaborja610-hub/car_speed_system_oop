class Car:
    def __init__(self, year_model,make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed

    def display_header(self):
        print("▀▄▀▄▀▄▀▄" * 6 + "\n")
        print(" " *15 + "Car Speed Status\n")
        print("▀▄▀▄▀▄▀▄" * 6 + "\n")
        print("A car entered the road.")
        print(f"Car Model: {self.__make} ({self.__year_model})")
        print("Car is ready!")
        print(f"Current Speed: {self.__speed} mph")