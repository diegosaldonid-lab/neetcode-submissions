from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        if n == 1:
            return [-1]
        

        r = n - 1
        curr_max = -1
        x = deque([])
        # [2,4,5,3,1,2]
        #  x = [5, 5, 3,2,2,-1]
        # curr_max = 5
        # r = 0
        # arr[r] = 2
        while r >= 0:
            x.appendleft(curr_max)
            curr_max = max(curr_max,arr[r])
            r-=1
        
        x = list(x)
        return x
