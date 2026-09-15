class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_st = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while mono_st and temperatures[i] > temperatures[mono_st[-1]]:
                popped = mono_st.pop()
                ans[popped] = i - popped
            mono_st.append(i)
        return ans