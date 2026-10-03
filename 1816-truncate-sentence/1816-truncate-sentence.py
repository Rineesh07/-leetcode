class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cnt = 0 
        ans = []
        for word in s.split(' '):
            print(word)
            if cnt == k :
                break
            ans.append(word)
            cnt += 1
        # ans = str(ans)
        return ' '.join(ans)