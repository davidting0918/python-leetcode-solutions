# https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            point, power = questions[i]

            solve = point + (dp[i + power + 1] if i + power + 1 < n else 0)
            skip = dp[i + 1]

            dp[i] = max(solve, skip)

        return dp[0]

if __name__ == "__main__":
    s = Solution()
    questions = [[3,2],[4,3],[4,4],[2,5]]
    print(s.mostPoints(questions))