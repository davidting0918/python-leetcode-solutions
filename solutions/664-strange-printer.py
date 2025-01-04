# https://leetcode.com/problems/strange-printer/description/?envType=daily-question&envId=2024-08-21
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        def _recursive(start: int, end: int):
            if start > end:
                return 0
            
            if dp[start][end] != -1:
                return dp[start][end]
            
            ans = 1 + _recursive(start + 1, end)
            first_s = s[start]

            for i in range(start + 1, end+1):
                if s[i] == first_s:  # if current char equals to first char then try if this is a better case
                    ans = min(
                        ans, 
                        _recursive(start, i - 1) + _recursive(i + 1, end)
                    )
            dp[start][end] = ans
            return ans
        
        return _recursive(0, n-1)
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.strangePrinter("aaabbb"))