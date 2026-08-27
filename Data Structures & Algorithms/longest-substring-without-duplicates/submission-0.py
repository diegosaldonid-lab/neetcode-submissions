class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        length = 1
        L = 0
        win = set(s[L])
        for R in range(1, n):
            while s[R] in win:
                win.remove(s[L])
                L += 1
            win.add(s[R])
            length = max(length, R - L + 1)


        return length