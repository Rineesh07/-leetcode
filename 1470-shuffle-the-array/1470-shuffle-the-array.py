class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        low = 0
        high = (n * 2)- 1
        mid = (low + high)//2
        num1 = []
        num2 = []
        for i in range(mid+1):
            num1.append(nums[i])
        print(num1)
        for j in range(mid+1,n*2):
            num2.append(nums[j])
        print(num2)
        ans = []
        for i in range(mid+1):
            ans.append(num1[i])
            ans.append(num2[i])
        return ans