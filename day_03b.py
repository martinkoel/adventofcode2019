# calculate all coordinates for wire 1
# calculate all coordinates for wire 2
# find coordinates that are the same for wire 1 and wire 2 (intersections)
# calculate the manhattan distance for the coordinates found and pick the closest intersection


def create_coord_list_from_instructions(instr_wire):
    coord_list = []
    x = 0
    y = 0

    for instr in instr_wire:

        direction = instr[0]
        positions = int(instr[1::])

        if direction == "R":
            for i in range(positions):
                x += 1
                new_coord = (x, y)
                coord_list.append(new_coord)
        elif direction == "L":
            for i in range(positions):
                x -= 1
                new_coord = (x, y)
                coord_list.append(new_coord)
        elif direction == "U":
            for i in range(positions):
                y += 1
                new_coord = (x, y)
                coord_list.append(new_coord)
        elif direction == "D":
            for i in range(positions):
                y -= 1
                new_coord = (x, y)
                coord_list.append(new_coord)
        else:
            print("Unknown instruction")

    return coord_list


f = open("day_03.txt", "r")
instr_wire_1_csv = f.readline()
instr_wire_2_csv = f.readline()
f.close()

#instr_wire_1_csv = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
#instr_wire_2_csv = "U62,R66,U55,R34,D71,R55,D58,R83"

coord_list_wire_1 = create_coord_list_from_instructions(instr_wire_1_csv.split(","))
coord_list_wire_2 = create_coord_list_from_instructions(instr_wire_2_csv.split(","))

print(len(coord_list_wire_1))
print(len(coord_list_wire_2))

#https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python#question14
print(list(set(coord_list_wire_1).intersection(coord_list_wire_2)))


