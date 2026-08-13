class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0 
        max_cnt = 0 
        for i in range(len(arr)):
            if arr[i] % 2 != 0 :
                cnt += 1
                max_cnt = max(cnt,max_cnt)
            else:
                cnt = 0 
        print(max_cnt)
        if max_cnt >= 3:
            return True
        else:
            return False
        