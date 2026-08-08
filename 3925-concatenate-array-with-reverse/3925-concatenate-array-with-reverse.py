class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        print(ans)
        j = len(nums) -1
        while j >= 0 :
            ans.append(nums[j])
            j -= 1
        return ans