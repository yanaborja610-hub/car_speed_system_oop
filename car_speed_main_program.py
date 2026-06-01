from car_class import Car

year = int(input("Enter year model:"))
make = input("Car brand:")

my_car = Car(year, make)

my_car.display_header()

# Acceleration
print("\nAcceleration Phase")
print("-" * 50)

for lap in range(1,6):
    my_car.accelerate()
    print(f"Lap {lap}: Speed = {my_car.get_speed()} mph")

print("\nMax speed reached!")

# Brake
print("\nBraking Phase")
print("-" * 50)

for brake in range(1,6):
    my_car.brake()
    print(f"Brake {brake}: Speed = {my_car.get_speed()} mph")

print("\nCar stopped.")
print("=" * 50)