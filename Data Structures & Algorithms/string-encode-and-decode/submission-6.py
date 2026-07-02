class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "<#EOS#>"
        return res
    def decode(self, s: str) -> List[str]:
        return s.split("<#EOS#>")[:-1]