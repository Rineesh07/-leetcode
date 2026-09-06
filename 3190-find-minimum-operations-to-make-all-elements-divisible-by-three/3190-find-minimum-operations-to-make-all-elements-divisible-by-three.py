class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for x in nums:
            if x % 3 != 0:
                cnt += 1
        print(cnt)
        # for i in range(n):
        #     print(min(nums[i] % 3, 3 - (nums[i] % 3)))
        return cnt