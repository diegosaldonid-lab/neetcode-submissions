class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        dp = [nums[0], nums[1]]

        for i in range(2,n):
            x3 = 0
            if i - 3 >= 0:
                x3 = dp[i - 3]
            x2 = dp[i - 2]
            dp.append(nums[i] + max(x2, x3))
        
        return max(dp[-1], dp[-2])
        