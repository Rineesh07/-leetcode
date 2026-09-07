class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        middle = 0
        n = len(nums)
        for i in range(n):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            print(left_sum,right_sum)
            if left_sum == right_sum :
                return i
        return -1