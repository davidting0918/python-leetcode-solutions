# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # logic sort the start and end time, if any intervals overlap, there must be a new group
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        end_ptr, group_count = 0, 0

        for start in start_times:
            if start > end_times[end_ptr]:
                end_ptr += 1
            else:
                group_count += 1

        return group_count

if __name__ == "__main__":
    s = Solution()
    intervals = [[159431,428743],[614908,651142],[431031,806494]]
    print(s.minGroups(intervals))