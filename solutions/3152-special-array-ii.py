# https://leetcode.com/problems/special-array-ii/description/
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        result = []

        adj = []
        for i in range(0, len(nums)-1):
            adj.append( 1 if nums[i] % 2 == nums[i+1] % 2 else 0)

        # 紀錄目前為止 parity 不同的組數
        prefix_sum = [0] * n

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + adj[i-1]


        for query in queries:
            start, end = query
            # 若在這段區間組數有增加 should return False
            if prefix_sum[end] - prefix_sum[start] == 0:
                result.append(True)
            else:
                result.append(False)
        return result

            

if __name__ == "__main__":
    s = Solution()
    nums = [3,4,1,2,6,7,8]
    queries = [[0, 4], [4, 6]]
    print(s.isArraySpecial(nums, queries)) # [True]