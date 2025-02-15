# https://leetcode.com/contest/biweekly-contest-150/problems/separate-squares-i/description/?slug=sum-of-good-numbers&region=global_v2

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum([i[2]**2 for i in squares])

        area_per = total_area / len(squares)
        return


if __name__ == "__main__":
    s = Solution()
    squares = [[0,0,2],[1,1,1]]
    print(s.separateSquares(squares))
