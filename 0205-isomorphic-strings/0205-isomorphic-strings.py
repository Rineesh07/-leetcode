class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot = {}
        ttos = {}
        for (a,b) in zip(s,t):
            if a in stot and stot[a] != b:
                return False
            if b in ttos and ttos[b] != a:
                return False

            stot[a] = b
            ttos[b] = a
        return True