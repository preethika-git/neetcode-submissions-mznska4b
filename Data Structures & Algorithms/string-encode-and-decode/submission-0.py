class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += strs[i] + "end"
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        i = 0
        while i < len(s):
            if i+2 <= len(s):
                if s[i] == "e" and s[i+1] == "n" and s[i+2] == "d":
                    strs.append(word)
                    word = ""
                    i+=3
                    continue
                else:
                    word += s[i]
                    i+=1

        return strs