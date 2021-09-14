def convert(s, numRows):
    output = [[] for i in range(numRows)]
    row = 0
    start = 0
    direction = 'forward'
    while start != len(s):
        print(row, s[start])
        output[row].append(s[start])
        if direction == 'forward':
            if row == len(output) - 1:
                direction = 'backward'
                row -= 1
            else:
                row += 1
        else:
            if row == 0:
                direction = 'forward'
                row += 1
            else:
                row -= 1
        start += 1
    outputString = ""
    for element in output:
        outputString += "".join(element)
    return outputString




print(convert("PAYPALISHIRING",4))