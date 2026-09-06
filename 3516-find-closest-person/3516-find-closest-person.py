class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first = abs(z-x)
        second = abs(z-y)
        print(first,second)
        if first < second:
            return 1
        elif first > second:
            return 2
        else:
            return 0