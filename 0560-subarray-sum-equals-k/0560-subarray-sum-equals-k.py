class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       prefixsum = 0 
       d = {0:1}
       subcnt = 0 
       for i in range(len(nums)):
           prefixsum += nums[i]
           req = prefixsum - k 
           if req in d:
               subcnt += d[req]
           d[prefixsum] = d.get(prefixsum,0) + 1
       return subcnt