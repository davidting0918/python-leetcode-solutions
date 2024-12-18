# https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-100-liked
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Logic: use in degree to determine whether current course can be taken now.
        # queue is to store the courses that can be taken now.
        # after taken each course, decrement the in degree of its neighbors, since the pre req is taken.
        # graphs[i] means after taking course i, which courses can be taken.

        graphs = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graphs[prereq].append(course)
            in_degree[course] += 1

        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        taken_courses = 0
        while queue:
            c_course = queue.pop(0)
            taken_courses += 1

            for neighbor in graphs[c_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return taken_courses == numCourses

if __name__ == "__main__":
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(s.canFinish(numCourses, prerequisites)) # False
