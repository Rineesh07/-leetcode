def present( a : List[int]  ,t : int) -> int:
    low =  0 
    n = len(a)
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == t:
            return mid
        elif a[mid] > t:
            high = mid - 1
        else:
            first = low
            low = mid + 1
    return low
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return present(nums,target)
        