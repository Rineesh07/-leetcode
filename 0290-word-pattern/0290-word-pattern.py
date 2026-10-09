class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False
        d = {}
        seen = {}
        for ch , word in zip(pattern,words):
            if ch in d and d[ch] != word:
                return False
            if word in seen and seen[word] != ch:
                return False
            d[ch] = word
            seen[word] = ch
        return True
