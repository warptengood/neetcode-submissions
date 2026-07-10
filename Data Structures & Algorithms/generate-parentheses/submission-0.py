class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        perm = []
        
        def check(s):
            st = []
            for c in s:
                if c == '(':
                    st.append(c)
                else:
                    if len(st) == 0 or st[-1] == ')':
                        return False
                    else:
                        st.pop()
            return len(st) == 0

        def rec(reml, remr):
            if reml == 0 and remr == 0:
                if check(perm):
                    result.append(''.join(perm))
                return
            if reml > 0:
                perm.append('(')
                rec(reml-1, remr)
                perm.pop()
            if remr > 0:
                perm.append(')')
                rec(reml, remr-1)
                perm.pop()

        rec(n, n)
        return result
