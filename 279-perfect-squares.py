# https://leetcode.com/problems/perfect-squares/description/?envType=study-plan-v2&envId=top-100-liked
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [
            float("inf") for _ in range(n+1)
        ]
        dp[0] = 0
        
        for i in range(1, n+1):
            # get the max square root of i
            target = math.floor(i ** (1/2)) 
            dp[i] = dp[i - target ** 2] + 1

            continue
            

        return dp[-1]
    

if __name__ == "__main__":
    s = Solution()
    n = 12
    print(s.numSquares(n)) # 3