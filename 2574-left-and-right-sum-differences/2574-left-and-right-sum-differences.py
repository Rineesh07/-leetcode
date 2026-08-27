import math
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left= []
        right = []
        rs = 0 
        rss = sum(nums)
        n = len(nums)
        for i in range(n):
            left.append(rs)
            rs += nums[i]
        for i in range(n):
            rss -= nums[i]
            right.append(rss)
        print(left,right)
        ans = []
        for i in range(n):
            a = abs(left[i]-right[i])
            ans.append(a)
        return ans
