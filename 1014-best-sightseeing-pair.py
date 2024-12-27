# https://leetcode.com/problems/best-sightseeing-pair/description/
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Logic: always use the max value (values[i] + i) to calculate the result
        # 1. Before update the max_value, calculate the result
        # 2. If the current value is the max value, update the max_value and do not need to calculate the result
        # 3. In each iteration and current != max_value, calculate the result
        #    (result = max(result, max_value - i + values[i]))
        n = len(values)

        max_value = 0
        result = 0
        for i in range(n):
            if i > 0:
                result = max(result, max_value - i + values[i])

            if values[i] + i > max_value:

                max_value = values[i] + i
                continue
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreSightseeingPair([8,1,5,2,6])) # 11