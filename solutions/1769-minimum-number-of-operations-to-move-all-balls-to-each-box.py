# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/?envType=daily-question&envId=2025-01-06
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        valid_index = [i for i in range(n) if boxes[i] == "1"]

        result = [0] * n

        for i in range(n):
            for index in valid_index:
                result[i] += abs(i - index)

        return result

    def minOperationsV2(self, boxes: str) -> List[int]:
        # use prefix and suffix sum to calculate the total operations needed for each box
        n = len(boxes)
        prefix_sum = [0] * n

        ball_count = 1 if boxes[0] == "1" else 0
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + ball_count
            if boxes[i] == "1":
                ball_count += 1

        suffix_sum = [0] * n
        ball_count = 1 if boxes[-1] == "1" else 0
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + ball_count
            if boxes[i] == "1":
                ball_count += 1

        return [prefix_sum[i] + suffix_sum[i] for i in range(n)]




if __name__ == "__main__":
    s = Solution()
    boxes = "110"
    print(s.minOperationsV2(boxes)) # [1,1,3]