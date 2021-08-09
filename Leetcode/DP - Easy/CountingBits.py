'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

'''

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        outputList = [0,1,1]
        # for i in range(n+1):
        #     num = i
        #     count = 0
        #     while num != 0:
        #         res = num % 2
        #         num = num//2
        #         if res == 1:
        #             count += 1
        #     outputList.append(count)
        # return outputList
        for i in range(3,n+1):
            if i % 2 == 0:
                outputList.append(outputList[i//2])
            else:
                outputList.append(outputList[i//2]+1)
        return outputList