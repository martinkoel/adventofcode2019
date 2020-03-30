f = open("day_01.txt", "r")

required_fuel = 0

for mass in f:
    fuel = (int(mass) // 3) - 2
    required_fuel += fuel

print(f"Required fuel: {required_fuel}")

f.close()
