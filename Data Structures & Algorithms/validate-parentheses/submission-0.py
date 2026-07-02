class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if len(st) == 0:
                st.append(c)
                continue
            if (
                st[-1] == '(' and c == ')' or
                st[-1] == '{' and c == '}' or
                st[-1] == '[' and c == ']'
            ):
                st.pop()
            else:
                st.append(c)
        return len(st) == 0