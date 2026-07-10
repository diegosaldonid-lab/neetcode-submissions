class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        pairs = {")":"(", "]":"[","}":"{"}
        for x in s:
            if len(a)>0 and (x in pairs) and pairs[x]== a[-1]:
                a.pop()
            else:
                a.append(x)

        return len(a) == 0