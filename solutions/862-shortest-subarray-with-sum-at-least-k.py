# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/?envType=daily-question&envId=2024-11-17
from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        queue = deque()
        min_len = float('inf')

        for i in range(n):
            prefix_sum += nums[i]

            if prefix_sum >= k:
                min_len = min(min_len, i + 1)

            while queue and prefix_sum - queue[0][0] >= k:
                min_len = min(min_len, i - queue[0][1])
                queue.popleft()

            while queue and prefix_sum <= queue[-1][0]:
                queue.pop()

            queue.append((prefix_sum, i))
            continue

        return min_len if min_len != float('inf') else -1

if __name__ == "__main__":
    s = Solution()
    nums = [2, -1, 2]
    k = 3
    print(s.shortestSubarray(nums, k))  # 3