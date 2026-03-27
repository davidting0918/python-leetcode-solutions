from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # length[i]: LIS of the current position
        # count[i]: number of LIS of the current position
        length = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] < length[j] + 1:  # use j as the new started is longer
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:  # from j is also a point to reach the length[i] length.
                        count[i] += count[j]

        # all count of LIS == max should be included in the answer
        max_length = max(length)
        return sum(c for l, c in zip(length, count) if l == max_length)

if __name__ == "__main__":
    s = Solution()
    print(s.findNumberOfLIS([1,3,5,4,7]))
    print(s.findNumberOfLIS([2,2,2,2,2]))