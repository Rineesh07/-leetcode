def candivide(nums: List[int] , k :  int , threshold : int) -> bool:
    summ = 0 
    for n in nums:
        summ += math.ceil(n/k)
    return summ <= threshold
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        low = 1
        high = max(nums)
        # print(candivide(nums,mid,threshold))
        while low < high:
            mid = (low+high)//2
            if candivide(nums,mid,threshold):
                high = mid
            else:
                low = mid + 1
        return low
