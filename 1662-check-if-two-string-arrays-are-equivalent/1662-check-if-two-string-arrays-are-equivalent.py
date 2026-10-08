class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        first = []
        second = []
        for word in word1:
            first.append(word)
        for word in word2:
            second.append(word)
        first = ''.join(first)
        second = ''.join(second)
        print(first,second)
        return first == second