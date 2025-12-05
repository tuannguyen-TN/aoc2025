import math

def getJoltage(bank):
    lastDigit = bank % 10
    bank //= 10
    
    prevLargest = lastDigit

    lastDigit = bank % 10
    bank //= 10

    currLargest = lastDigit

    while bank > 0:
       lastDigit = bank % 10
       bank //= 10

       if lastDigit >= currLargest:
           prevLargest = max(prevLargest, currLargest)
           currLargest = lastDigit

    return currLargest * 10 + prevLargest


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        content = list(map(int, f.readlines()))
        total = 0

        for num in content:
            print(num, getJoltage(num))
            total += getJoltage(num)

        print(total)
