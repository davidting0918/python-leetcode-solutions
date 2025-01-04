# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05
from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # first exclude the impossible cases
        # 1. even the left all be 6 still can't reach the mean
        # 2. even the left all be 1 still be greater than the mean

        target = mean * (len(rolls) + n) - sum(rolls)

        # check if the target is possible
        if target < n or target > 6 * n:
            return []

        avg = target // n
        result = [avg] * n
        remainder = target % n
        for i in range(remainder):
            result[i] += 1
        return result


if __name__ == "__main__":
    s = Solution()
    rolls = [1, 5, 6]
    mean = 3
    n = 4
    print(s.missingRolls(rolls, mean, n))