class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        const = 0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    break
            else:
                const += 1
        return const