import math

def getJoltage(bank, n):
    stack = []

    for i in range(n):
        lastDigit = bank % 10
        bank //= 10
        stack.append(lastDigit)

    while bank > 0:
        lastDigit = bank % 10
        bank //= 10
        temp_stack = []

        while stack and lastDigit >= stack[-1]:
           temp_stack.append(lastDigit)
           lastDigit = stack.pop()

        while temp_stack:
            stack.append(temp_stack.pop())
            
    result = 0
    while stack:
        result = result * 10 + stack.pop()

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        content = list(map(int, f.readlines()))
        total = 0

        for num in content:
            total += getJoltage(num, 12)

        print(total) 
