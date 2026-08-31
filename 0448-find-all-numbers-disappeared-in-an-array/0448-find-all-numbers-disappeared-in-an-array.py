class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = {}
        n = len(nums)
        ans = []
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        print(d)
        for i in range(1,n+1):
            if i not in d:
                ans.append(i)
        return ans