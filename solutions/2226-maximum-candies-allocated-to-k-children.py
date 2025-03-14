# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        # use binary search to find the maximum number of candies that can be allocated to each child
        left, right = 1, max(candies)
        while left < right:
            mid = (left + right + 1) // 2

            possible = 0
            for i in candies:
                possible += i // mid
            
            if possible >= k:
                left = mid
            else:
                right = mid - 1
        return left
    
if __name__ == "__main__":
    s = Solution()
    candies = [5,8,6]
    k = 3
    print(s.maximumCandies(candies, k))

