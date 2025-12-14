with open("input.txt", "r") as f:
    content = f.readlines()
    matrix = []
    for i in range(len(content)):
        tempArr = []

        if i != len(content) - 1:
            left, right = 0, 0

            while left < len(content[i]):
                while left < len(content[i]) and not content[i][left].isnumeric():
                    left += 1

                for right in range(left, len(content[i])):
                    if not content[i][right].isnumeric():
                        tempArr.append(int(content[i][left:right]))
                        left = right
                        break

        else:
            for j in range(len(content[i])):
                if content[i][j] in ("+", "*"):
                    tempArr.append(content[i][j])

        matrix.append(tempArr)

    ROWS, COLS = len(matrix), len(matrix[0])
    total = 0

    for col in range(COLS):
        operation = lambda x, y: x + y
        startingValue = 0

        if matrix[ROWS - 1][col] == "*":
            operation = lambda x,y: x * y
            startingValue = 1

        for row in range(ROWS - 1):
            startingValue = operation(startingValue, matrix[row][col])

        total += startingValue

    print(total)
