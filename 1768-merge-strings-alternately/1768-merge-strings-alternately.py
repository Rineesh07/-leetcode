class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = []
        m1 = len(word1)
        m2 = len(word2)
        m = min(m1,m2)
        for i in range(m):
            merge.append(word1[i])
            merge.append(word2[i])
        n = abs(m1-m2)
        string = 'equal'
        if m1 < m2:
            string = 'second'
        elif m2 < m1:
            string = 'first'
        print(merge)
        if string == 'equal':
            return ''.join(merge)
        elif string == 'first':
            for i in range(m,m1):
                merge.append(word1[i])
            return ''.join(merge)
        else:
            for i in range(m,m2):
                merge.append(word2[i])
            return ''.join(merge)