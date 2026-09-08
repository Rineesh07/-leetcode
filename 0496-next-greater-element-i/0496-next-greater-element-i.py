class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        monostack = []
        for n in nums2:
            if not monostack:
                monostack.append(n)
            else:
                while monostack and n > monostack[-1]:
                    nge[monostack[-1]] = n
                    monostack.pop()
                monostack.append(n)
        print(nge)
        ans = []
        for n in nums1:
            if n in nge:
                ans.append(nge[n])
            else:
                ans.append(-1)
        return ans
            
