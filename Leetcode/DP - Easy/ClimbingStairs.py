class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        n1, n2 = 1, 2
        for i in range(3,n+1):
            new = n1 + n2
            n1, n2 = n2, new
        return n2