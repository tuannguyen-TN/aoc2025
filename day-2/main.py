def rotate(currNum, direction, steps):
    if direction == "R":
        currNum += steps
    else:
        currNum -= steps

    return currNum % 100


num = 50
total = 0

with open("input.txt", "r") as f:
    content = f.readlines()
    for instruction in content:
        dir, steps = instruction[0], int(instruction[1:])
        num = rotate(num, dir, steps)
        total += steps // 100
        if num == 0:
            total += 1

print(total)
