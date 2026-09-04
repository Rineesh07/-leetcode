class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0 
        while i < n - 1 :
            j = i + 1
            if nums[i] == nums[j]:
                nums[i] = nums[i] * 2
                nums[j] = 0
            i += 1
        print(nums)
        ans = []
        for x in nums:
            if x != 0:
                ans.append(x)
        print(ans)
        zeros = n - len(ans)
        print(zeros)
        for i in range(zeros):
            ans.append(0)
        return ans