class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = [-1] * 26
        r = [-1] * 26
        for i, c in enumerate(s):
            if l[ord(c) - 97] == -1:
                l[ord(c) - 97] = i
            r[ord(c) - 97] = i
        res = []
        cur_l, cur_r = -1, -1
        for i in range(len(s)):
            print(f"Current letter is {s[i]}, l={l[ord(s[i]) - 97]}, r={r[ord(s[i]) - 97]}. Prev range is {cur_l} and {cur_r}.")
            next_l, next_r = l[ord(s[i]) - 97], r[ord(s[i]) - 97]
            if cur_r < next_l:
                if i > 0:
                    res.append(cur_r - cur_l + 1)
                cur_l, cur_r = next_l, next_r
            else:
                cur_r = max(cur_r, next_r)
        res.append(cur_r - cur_l + 1)
        return res