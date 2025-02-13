# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13
from multiprocessing.connection import answer_challenge
from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0

        heapq.heapify(nums)
        while True:
            if len(nums) < 2:
                return answer
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)

            if n1 >= k and n2 >= k:
                return answer

            heapq.heappush(nums, min(n1, n2) * 2 + max(n1, n2))
            answer += 1

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2,4,9]
    k = 20
    print(s.minOperations(nums, k))