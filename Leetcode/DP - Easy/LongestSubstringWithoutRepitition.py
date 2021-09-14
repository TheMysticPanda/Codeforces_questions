def lengthOfLongestSubstring(s):
    start = 0
    end = start
    longest = 0
    characters = {}

    a = ord("a")
    z = ord("z")
    
    while a != z+1:
        characters[chr(a)] = 0
        a+=1
  

    while end != len(s):
        #if character is in the dictionary
        if characters[s[end]] == 1:
            characters[s[start]] -= 1
            start += 1
        #if character isn't in the dictionary
        else:
            characters[s[end]] = 1
            end += 1
        if end - start > longest:
            longest = end-start
    return longest

 
        

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("abcbb"))