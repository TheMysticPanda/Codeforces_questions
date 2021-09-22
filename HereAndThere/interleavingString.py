class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        p1 = 0
        p2 = 0
        p3 = 0
        while p3 != len(s3) and p1 != len(s1) and p2 != len(s2):
            if s3[p3] == s1[p1] and s3[p3] != s2[p2] :
                p3 += 1
                p1 += 1
            elif s3[p3] == s2[p2] and s3[p3] != s1[p1]:
                p3 += 1
                p2 += 1
            elif s3[p3] == s1[p1] == s2[p2]:
                if s3[p3+1] == s2[p2+1]:
                    p3 += 2
                    p2 += 2
                elif s3[p3+1] == s1[p1+1]:
                    p3 += 2
                    p1 += 2
                else:
                    return False 
            else:
                return False
        if p1 == len(s1):
            #check for remaining characters of s2
            while p3 != len(s3):
                if s3[p3] != s2[p2]:
                    return False
                p3 += 1
                p2 += 1
        elif p2 == len(s2):
            #check for remaining characters of s1
            while p3 != len(s3):
                if s3[p3] != s1[p1]:
                    return False
                p3 += 1
                p1 += 1
        return True

solution = Solution()
print(solution.isInterleave("aabcc","dbbca","aadbbcbcac"))
print(solution.isInterleave("aabcc","dbbca","aadbbbaccc"))
print(solution.isInterleave("","",""))
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true