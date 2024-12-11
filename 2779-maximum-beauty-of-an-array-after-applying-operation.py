# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/?envType=daily-question&envId=2024-12-11
from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num - k, 1))  # Start of range
            events.append((num + k + 1, -1))  # End of range
            
        events.sort()

        # Use a sweep line approach to calculate the maximum overlap
        max_beauty = 0
        current_count = 0
        for value, effect in events:
            current_count += effect
            max_beauty = max(max_beauty, current_count)

        return max_beauty


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 1]
    k = 10
    print(s.maximumBeauty(nums, k)) # 13