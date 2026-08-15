class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = [(value , i) for i , value in enumerate(nums)]
        print(ind)
        ind.sort()
        nums.sort()
        i = 0 
        j = len(nums) - 1
        while i < j :
            s = nums[i] + nums[j]
            if s == target:
                return ind[i][1] , ind[j][1]
            elif s < target :
                i += 1
            else:
                j -= 1
        