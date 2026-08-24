class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p = 0
        ls = 0 
        n = len(nums)
        sumleft = [] 
        sumright = [sum(nums)]
        rs = sum(nums)
        for i in range(len(nums)):
            ls += nums[i]
            sumleft.append(ls)
        for i in range(len(nums)-1):
            rs -= nums[i]
            sumright.append(rs)
        print(sumleft,sumright)
        for i in range(len(nums)):
            if sumleft[i] == sumright[i]: 
                return i
        return -1
        