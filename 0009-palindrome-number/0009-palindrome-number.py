class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0 
        o = x
        while x > 0 :
            d = x % 10
            rev = rev * 10 + d
            x //= 10
        if rev == o :
            return True
        else:
            return False


        