# https://leetcode.com/problems/rank-transform-of-an-array/description/
from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))

        rank_map = {}
        for i in range(len(sorted_arr)):
            rank_map[sorted_arr[i]] = i + 1

        output = []
        for i in arr:
            output.append(rank_map[i])
        return output


if __name__ == "__main__":
    s = Solution()
    arr = [40,10,20,30]
    print(s.arrayRankTransform(arr))