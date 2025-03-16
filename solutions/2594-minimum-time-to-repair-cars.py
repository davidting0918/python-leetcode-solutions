# https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16
from typing import List
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # use binary search to find minimum time
        left = 1
        right = min(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2
            print(left, mid, right)

            if self.can_repair(ranks, cars, mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def can_repair(self, ranks: List[int], cars: int, time: int) -> bool:
        count = 0
        for i in range(len(ranks)):
            count += int(
                (time / ranks[i]) ** 0.5
            )
        return count >= cars

if __name__ == "__main__":
    solution = Solution()
    print(solution.repairCars([4, 2, 3, 1], 10))

