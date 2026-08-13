class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0 
        current_sum = 0 
        max_avg = -1000000 
        cur_avg = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            if right >= k - 1:
                cur_avg = current_sum /k
                max_avg = max(cur_avg , max_avg) 
                current_sum -= nums[left]
                left += 1
        return max_avg        