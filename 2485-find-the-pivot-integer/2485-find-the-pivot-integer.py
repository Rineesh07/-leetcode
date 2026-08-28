class Solution:
    def pivotInteger(self, n: int) -> int:
        a = [0]
        b = []
        for i in range(1,n+1):
            a.append(i)
        for i in range(1,n+1):
            b.append(i)
        prefix = []
        suffix = []
        rs = 0 
        ss = sum(a) 
        for i in range(n):
            rs += b[i]
            prefix.append(rs)
        for i in range(n):
            ss -= a[i]
            suffix.append(ss)
        print(prefix,suffix)
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i + 1
        return -1
