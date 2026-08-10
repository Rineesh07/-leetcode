class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = []
        for i in range(len(nums)):
            s.append(nums[i]*nums[i])
        s.sort()
        return s

        