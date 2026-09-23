class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        total = 0
        for i in range(n):
            nums[i] = start + 2 * i
        xor = 0 
        for x in nums:
            xor = x ^ xor
        return xor