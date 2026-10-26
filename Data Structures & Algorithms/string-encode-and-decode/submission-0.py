class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + ":" + s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i < len(s)):
            j = i
            while s[j] != ":":
                j += 1
            fetch_length_ofstr_peice = int(s[i:j])
            i = j+1
            j = i + fetch_length_ofstr_peice
            res.append(s[i:j])
            i=j

        return res