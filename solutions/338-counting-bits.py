# https://leetcode.com/problems/counting-bits/description/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Logic: In each round (2**(i-1) to 2**i), the number of 1s is the same as the number of 1s in the previous round (0 to 2**(i-1)) plus 1.
        and in since each round has different lengthm we need to keep track of the offset.
        """
        dp = [0] * (n+1)
        
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i 
            dp[i] = dp[i-offset] + 1
        return dp
    
if __name__ == "__main__":
    s = Solution()
    print(s.countBits(5)) # [0,1,1,2,1,2]
    