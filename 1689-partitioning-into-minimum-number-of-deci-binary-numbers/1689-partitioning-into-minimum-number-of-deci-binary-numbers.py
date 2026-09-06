class Solution:
    def minPartitions(self, n: str) -> int:
        nums = []
        for num in n:
            num = int(num)
            nums.append(num)
        print(nums)
        return max(nums)