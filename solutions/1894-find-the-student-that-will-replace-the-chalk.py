# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=daily-question&envId=2024-09-02
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        remainder = k % total

        for i in range(len(chalk)):
            if remainder < chalk[i]:
                return i
            remainder -= chalk[i]
        return remainder


if __name__ == "__main__":
    s = Solution()
    chalk = [5,1,5]
    k = 22
    print(s.chalkReplacer(chalk, k)) # 0