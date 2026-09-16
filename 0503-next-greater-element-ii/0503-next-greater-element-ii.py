class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n  = len(nums)
        st = []
        ans = [-1] * n
        for i in range(n*2):
            idx = i % n
            if not st:
                st.append(idx)
            else:
                while st and nums[st[-1]] < nums[idx]:
                    nge = st.pop()
                    ans[nge] = nums[idx]
                st.append(idx)
        return ans