class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textdict = {}
        for ch in text:
            if ch in textdict:
                textdict[ch] += 1
            else:
                textdict[ch] = 1
        s = 'ballon'
        for k in list(textdict.keys()):
            if k not in s:
                del textdict[k]
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
            else:
                m.append(v)
        print(m)
        return (min(m))