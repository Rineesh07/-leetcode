class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rp = 1
        suffix = [1]
        prefix = [1]
        for num in nums:
            rp *= num
            prefix.append(rp)
        prefix = prefix[:n]
        ans = []
        rp = 1
        for i in range(n-1,-1,-1):
            suffix.append(rp)
            rp *= nums[i]
        suffix.reverse()
        suffix = suffix[:n]
        print(prefix,suffix)
        for i in range(n):
            ans.append(prefix[i]*suffix[i])
        return ans
        