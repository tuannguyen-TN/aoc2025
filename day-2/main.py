def checkInvalid(id):
    n = len(id)

    for i in range(1, n // 2 + 1):
        for j in range(0, n - i, i):
            if id[j:j+i] != id[j+i:j+i+i]:
                break
        else:
            return True

    return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        content = f.read().strip()
        ranges = content.split(",")

        total = 0

        for num_range in ranges:
            start, end = list(map(int, num_range.split("-")))
            for i in range(start, end + 1):
                if checkInvalid(str(i)):
                    total += i

        print(total)
