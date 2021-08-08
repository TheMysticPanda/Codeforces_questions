def getMaximumGenerated(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    lst = [0,1]
    for i in range(2,n+1):
        if i%2 == 0:
            lst.append(lst[i//2])
        else:
            lst.append(lst[i//2] + lst[(i//2) + 1])

    return max(lst)
print(getMaximumGenerated(7))