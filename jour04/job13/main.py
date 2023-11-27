L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

resultantList = []

for element in L:
    found = False
    for item in resultantList:
        if item == element:
            found = True
            break
    if not found:
        resultantList = resultantList + [element]

print(resultantList)