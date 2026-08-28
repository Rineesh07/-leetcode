class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in d:
                d[key] = []
            d[key].append(word)
        for v in d.values():
            ans.append(v)
        return ans