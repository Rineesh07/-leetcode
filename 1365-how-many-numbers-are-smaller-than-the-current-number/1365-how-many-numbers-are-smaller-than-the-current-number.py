class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            cnt = 0 
            max_cnt =0
            for j in range(n):
                # cnt = 0
                if i != j:
                    if nums[j] < nums[i]:
                        cnt += 1
                    max_cnt = max(cnt,max_cnt)
            print(max_cnt)
            ans.append(max_cnt)
        return ans
                    
            
        
        