
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 :
            sign = -1
        else: 
            sign = 1
        x = abs(x)
        s = 0 
        rev = 0 
        while x > 0:
            d = x % 10 
            rev =  rev * 10 +d
            x = x//10

        rev *= sign
        if rev < -2 ** 31 or rev > (2 ** 31) - 1 :
            return 0
        return rev


        