num = 50
total = 0

with open("input.txt", "r") as f:
    content = f.readlines()
    for instruction in content:
        dir, steps = instruction[0], int(instruction[1:])

        while steps > 0:
            if dir == "R":
                num += 1
            else:
                num -= 1

            num %= 100
            if num == 0:
                total += 1

            steps -= 1

print(total)
