def myAtoi(s):
    positive = True
    start = 0
    end = len(s)
    for i in range(len(s)):
        if s == " ":
            start += 1
        elif s == "-":
            start += 1
            positive = False
        if s[i].isalpha():
            end = i
            break
    if end-start == 0:
        return 0
    if not positive:
        return int(s[start:end])
    else:
        return int(s[start:end])*(-1)

print(myAtoi("42"))
print(myAtoi("    -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))