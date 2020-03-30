f = open("day_02.txt", "r")

int_codes_string = f.readline()
f.close()

int_codes = list(map(int, int_codes_string.split(',')))

# replace values, as per instruction
int_codes[1] = 12
int_codes[2] = 2

pos = 0
do_loop = True

while do_loop:

    if int_codes[pos] == 1:
        result = int_codes[int_codes[pos + 1]] + int_codes[int_codes[pos + 2]]
        int_codes[int_codes[pos + 3]] = result
    elif int_codes[pos] == 2:
        result = int_codes[int_codes[pos + 1]] * int_codes[int_codes[pos + 2]]
        int_codes[int_codes[pos + 3]] = result
    elif int_codes[pos] == 99:
        do_loop = False
    else:
        print("unknown code")

    pos += 4


print(int_codes)


