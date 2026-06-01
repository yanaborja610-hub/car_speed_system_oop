from car_class import Car

year = int(input("Enter year model:"))
make = int(input("Car brand:"))

my_car = Car(year, make)

my_car.display_header()