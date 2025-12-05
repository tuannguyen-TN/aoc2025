def countNeighbors(x, y, grid):
    ROWS, COLS = len(grid), len(grid[0])

    total = 0

    DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for dx, dy in DIRECTIONS:
        row, col = x + dx, y + dy
        if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == "@":
            total += 1

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        content = [[c for c in s.strip()] for s in f.readlines()]
        ROWS, COLS = len(content), len(content[0])
   
        total = 0
        while True:
            subTotal = 0

            for r in range(ROWS):
                for c in range(COLS):
                    if content[r][c] == "@" and countNeighbors(r, c, content) < 4:
                        subTotal += 1
                        content[r][c] = "."

            if subTotal == 0:
                break

            total += subTotal

        print(total)
