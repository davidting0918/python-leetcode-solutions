# https://leetcode.com/problems/alternating-groups-ii/?envType=daily-question&envId=2025-03-09
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:(k-1)])
        count = 0
        left = 0

        for right in range(len(colors)): # make sure every subarray is a new one
            if right > 0 and colors[right] == colors[right-1]:
               # reset left and right
               left = right

            if right - left + 1 >= k:  # no need to make sure every subarray length is k
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    color = [0,1,0,1,0]
    k = 3
    print(s.numberOfAlternatingGroups(color, k))
