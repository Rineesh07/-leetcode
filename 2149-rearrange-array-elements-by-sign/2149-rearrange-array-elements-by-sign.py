class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        result = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            elif nums[i] > 0 :
                pos.append(nums[i])
        print(neg,pos)
        i = 0 
        j = 0 
        while i < len(pos) :
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1
        return result