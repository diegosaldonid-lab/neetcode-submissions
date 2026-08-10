class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ret = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            ret = max(ret, curr)


        return ret

        
        