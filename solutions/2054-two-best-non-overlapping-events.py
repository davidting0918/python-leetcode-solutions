# https://leetcode.com/problems/two-best-non-overlapping-events/description/?envType=daily-question&envId=2024-12-08
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])

        prefix_max = []
        max_value = 0
        result = 0

        for start, end, value in events:
            # use binary search to find the largest value before the start of the current event
            left, right = 0, len(prefix_max) - 1
            valid_index = -1
            while left <= right:
                mid = (left + right) // 2
                if prefix_max[mid][0] < start:
                    valid_index = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if valid_index != -1:
                result = max(
                    result, prefix_max[valid_index][1] + value
                )
            else:
                result = max(result, value)
            max_value = max(max_value, value)
            prefix_max.append((end, max_value))
        return result

if __name__ == '__main__':
    s = Solution()
    events = [[1,3,2],[4,5,2],[2,4,3]]
    print(s.maxTwoEvents(events)) # 6