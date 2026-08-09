class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        fin = []
        for n in order:
            for ch in friends:
                if n == ch :
                    fin.append(n)
        return fin
        