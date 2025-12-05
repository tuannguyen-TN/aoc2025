with open("input.txt", "r") as f:
    content = f.readlines()
    emptyLineIndex = 0
    for i in range(len(content)):
        if content[i] == "\n":
            emptyLineIndex = i

    ranges = [content[i].strip() for i in range(emptyLineIndex)]
    # ids = [int(content[i].strip()) for i in range(emptyLineIndex + 1, len(content))]
    
    pairs = []
    for numRange in ranges:
        nums = numRange.split("-")
        start, end = int(nums[0]), int(nums[1])
        pairs.append([start, end])

    pairs.sort()
    nonOverlappingPairs = [pairs[0]]

    for i in range(1, len(pairs)):
        newStart, newEnd = pairs[i]
        currStart, currEnd = nonOverlappingPairs[-1]
        
        if currStart <= newStart <= currEnd:
            nonOverlappingPairs[-1][0] = min(currStart, newStart)
            nonOverlappingPairs[-1][1] = max(currEnd, newEnd)
        else:
            nonOverlappingPairs.append([newStart, newEnd])
    
    count = 0
    for start, end in nonOverlappingPairs:
        count += end - start + 1
    print(count)




    # for id in ids:
    #     for start, end in pairs:
    #         if id < start:
    #             break
    #
    #         if start <= id <= end:
    #             count += 1
    #             break
    #
    # print(count)
