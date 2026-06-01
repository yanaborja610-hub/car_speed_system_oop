from car_class import Car

print(" ")
year = int(input("Enter year model: "))
make = input("Car brand: ")
print(" ")
my_car = Car(year, make)

my_car.display_header()

# Acceleration
print("\n\033[91mACCELERATION PHASE\033[0m")
print("-" * 48)

for lap in range(1,6):
    my_car.accelerate()
    print(f"Lap {lap}: Speed = {my_car.get_speed()} mph")

print("\nMax speed reached!")

# Brake
print("\n\033[91mBRAKING PHASE\033[0m")
print("-" * 48)

for brake in range(1,6):
    my_car.brake()
    print(f"Brake {brake}: Speed = {my_car.get_speed()} mph")

print("\nCar stopped.")
print("=" * 48)