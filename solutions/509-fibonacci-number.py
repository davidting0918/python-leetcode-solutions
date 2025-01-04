# https://leetcode.com/problems/fibonacci-number/description/
class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    def _r_fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self._r_fib(n-1) + self._r_fib(n-2)

if __name__ == "__main__":
    s = Solution()
    print(s.fib(3))

    
