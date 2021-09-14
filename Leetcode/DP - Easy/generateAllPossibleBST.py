def generateBinarySearchTrees(inputList):
    if len(inputList) == 0:
        return [[]]
    if len(inputList) == 1:
        return [[inputList[0]]]
    outputList = []
    for i in range(len(inputList)):
        # print(inputList[0:i-0])
        left = generateBinarySearchTrees(inputList[0:i-0])
        # print("left",left)
        # print(inputList[i+1:len(inputList)-i])
        right = generateBinarySearchTrees(inputList[i+1:len(inputList)-i])
        # print("right",right)
        if i == 0:
            innerList = [inputList[0], "null"]
        else:
            innerList = [inputList[i]]
        # print("innerList",innerList)
        for element in left:
            # print(element)
            lefthalf = element.extend(innerList)
            # print("element", element)
            outputList.append(element)
        # print(outputList)
        print(outputList)
        for element in right:
            for value in outputList:
                value.extend(element)
    return outputList

print(generateBinarySearchTrees([1,2]))