class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        good_pairs = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            for j in range(m):
                # print(nums1[i],nums2[j])
                eq = nums2[j] * k
                if nums1[i] % eq == 0 :
                    good_pairs += 1
        return good_pairs