# https://leetcode.com/contest/biweekly-contest-137/problems/find-the-power-of-k-size-subarrays-i/description/
from typing import List

class Solution:
    def findThePowerOfKSizeSubarrays(self, nums: List[int], k: int) -> int:
        """
        This method will still cause TLE. need to optimize the sorted part.
        """
        results = []

        if k == 1:
            return nums

        sub = nums[:k - 1]
        for i in range(k - 1, len(nums)):
            sub.append(nums[i])
            if sub[-1] != sub[0] + k - 1:
                results.append(-1)
            elif sorted(sub) != sub:
                results.append(-1)
            elif len(set(sub)) != k:
                results.append(-1)
            else:
                results.append(sub[-1])
            sub.pop(0)
        return results

if __name__ == "__main__":
    s = Solution()
    print(s.findThePowerOfKSizeSubarrays([1,2,3,4,3,3,5], 3))