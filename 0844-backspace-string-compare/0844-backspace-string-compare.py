class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        for ch in s:
            if ch == '#':
                if st:
                    st.pop()
            else:
                st.append(ch)
        st = ''.join(st)
        st2 = []
        for ch in t:
            if ch == '#':
                if st2:
                    st2.pop()
            else:
                st2.append(ch)
        st2 = ''.join(st2)
        return st == st2