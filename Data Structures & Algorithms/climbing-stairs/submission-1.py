class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        memo = {1:1,2:2}
        return self.recurse(memo, n-1) + self.recurse(memo,n-2)
    
    def recurse(self,memo,n):
        if n in memo:
            return memo[n]
        
        memo[n] = self.recurse(memo, n-1) + self.recurse(memo,n-2)
        return memo[n]