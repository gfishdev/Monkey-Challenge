def collect_bananas(jungle):
    sum = 0
    listPath = []
    lastLine = None

    for col in range(len(jungle[0])):
        greatestValue = None
        lineGreatestValue = 0
        if lastLine is None:
            for line in range(len(jungle)):
                if greatestValue is None or jungle[line][col] > greatestValue:
                    greatestValue = jungle[line][col]
                    lineGreatestValue = line
        else:
            greatestValue = jungle[lastLine][col]

            if lastLine > 0 and jungle[lastLine - 1][col] > greatestValue:
                greatestValue = jungle[lastLine - 1][col]
                lineGreatestValue = lastLine - 1

            if lastLine < len(jungle) - 1 and jungle[lastLine + 1][col] > greatestValue:
                greatestValue = jungle[lastLine + 1][col]
                lineGreatestValue = lastLine + 1

        listPath.append(str(lineGreatestValue) + ", " + str(col))
        lastLine = lineGreatestValue
        sum += greatestValue
        print(greatestValue)

    print(sum)
    print(listPath)


print("sample 1: ")
collect_bananas([[1, 3, 3], [2, 1, 4], [0, 6, 4]])
print("sample 2: ")
collect_bananas([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]])
print("sample 3: ")
collect_bananas([[10, 33, 13, 15], [22, 21, 4, 1], [5, 0, 2, 3], [0, 6, 14, 2]]