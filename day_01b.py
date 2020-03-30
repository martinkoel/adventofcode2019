f = open("day_01.txt", "r")

required_fuel = 0


def calculate_fuel(mass_in):
    return (int(mass_in) // 3) - 2


for mass in f:

    mass_to_use = mass

    while calculate_fuel(mass_to_use) > 0:
        fuel = calculate_fuel(mass_to_use)
        required_fuel += fuel
        mass_to_use = fuel


print(f"Required fuel: {required_fuel}")

f.close()



