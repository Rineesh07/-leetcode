def ispalindrome(a : List[int]):
    n = len(a)
    left = 0 
    right = n - 1
    n = len(a)
    while left <= right:
        if a[left] == a[right]:
            flag = True
        else:
            flag = False
            break
        left += 1
        right -= 1
    return flag
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if ispalindrome(s):
            return 1
        else:
            return 2