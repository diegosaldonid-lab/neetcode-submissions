class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        w = 0
        n = len(nums)

        for r in range(len(nums)):
            if nums[r] != val:
                k+=1
                nums[w] = nums[r]
                w+=1


        return k
        