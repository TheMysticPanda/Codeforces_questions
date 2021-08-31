def cuttingRod(prices, length):
    if length == 0:
        return 0
    else:
        maxValue = 0
        for i in range(1,length):
           maxValue =  max(maxValue, cuttingRod(prices, length-i-1)+prices[i])
        return maxValue

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cuttingRod(arr, size))
