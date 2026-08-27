class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        n = len(nums)
        length = n + 1
        win_total = 0
        for R in range(n):
            win_total += nums[R]
            while win_total >= target:
                length = min (length, R - L + 1)
                win_total -= nums[L]
                L += 1
        return 0 if length == n + 1 else length
        