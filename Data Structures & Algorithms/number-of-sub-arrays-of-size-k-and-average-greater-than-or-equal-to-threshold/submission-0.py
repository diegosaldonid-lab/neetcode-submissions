class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        L = 0 
        passed = 0
        n = len(arr)

        for R in range(n):
            if R - L + 1 > k:
                window_sum -= arr[L]
                L += 1
            window_sum += arr[R]
            if (R - L + 1) == k and window_sum / k >= threshold:
                passed += 1


        return passed
        