class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0 
        rs = 0 
        ans = [0]
        for i in range(len(gain)):
            rs += gain[i]
            ans.append(rs)
        print(ans)
        high = max(ans)
        return high

            
