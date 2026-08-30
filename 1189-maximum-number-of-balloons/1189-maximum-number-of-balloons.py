class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textdict = {}
        for ch in text:
            if ch in textdict:
                textdict[ch] += 1
            else:
                textdict[ch] = 1
        print(textdict)
        m = []
        if len(textdict) < 5:
            return 0
        for k,v in textdict.items():
            if k == 'b':
                m.append(v)
            elif k == 'a':
                m.append(v)
            elif k == 'l':
                m.append(v//2)
            elif k == 'o':
                m.append(v//2)
            elif k == 'n':
                m.append(v)
        print(m)
        if len(m) < 5:
            return 0
        return (min(m))