# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        
        colors_map = {}  # how many balls of each color
        balls = {}  # what color is each ball
        colors = set()  # all distinct colors

        answers = []
        for i in range(n):
            b, c = queries[i]

            if b in balls:
                colors_map[balls[b]] -= 1
                if colors_map[balls[b]] == 0:
                    colors.remove(balls[b])
            balls[b] = c
            colors_map[c] = colors_map.get(c, 0) + 1
            colors.add(c)
            answers.append(len(colors))
        return answers

if __name__ == "__main__":
    s = Solution()
    limit = 4
    queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
    print(s.queryResults(limit, queries))