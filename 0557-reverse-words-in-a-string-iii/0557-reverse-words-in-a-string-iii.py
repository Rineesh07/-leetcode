class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        ans = []
        for word in words:
            word = word[::-1]
            ans.append(word)
        print(ans)
        return ' '.join(ans)
