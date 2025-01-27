# https://leetcode.com/problems/course-schedule-iv/description/?envType=daily-question&envId=2025-01-27
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        return

if __name__ == "__main__":
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1], [1, 0]]
    print(s.checkIfPrerequisite(numCourses, prerequisites, queries)) # [False, True]
