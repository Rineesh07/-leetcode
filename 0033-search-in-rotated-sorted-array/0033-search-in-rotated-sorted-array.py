class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        d = {}
        for i , v in enumerate(nums):
            d[v] = i
        print(d)
        nums.sort()
        low = 0 
        high = n - 1
        while low <= high :
            mid = (low+high)//2
            if nums[mid] == target:
                return d[target]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
        