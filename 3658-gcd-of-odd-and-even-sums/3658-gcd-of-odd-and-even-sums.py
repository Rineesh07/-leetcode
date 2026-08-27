class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = []
        odd = []
        e_cnt = 0 
        o_cnt = 0 
        i = 0
        while e_cnt <= n and o_cnt <= n:
            if i % 2 == 0:
                even.append(i)
                i += 1
                e_cnt += 1
            else:
                odd.append(i)
                i += 1
                o_cnt += 1
        print(odd,even)
        a = sum(odd)
        b = sum(even)
        while b != 0 :
            a , b = b , a % b 
        return a 

        