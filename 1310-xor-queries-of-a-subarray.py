# https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=daily-question&envId=2024-09-13
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix_sum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_sum[i+1] = prefix_sum[i] ^ arr[i]
        
        results = []
        
        for i in range(len(queries)):
            results.append(prefix_sum[queries[i][0]] ^ prefix_sum[queries[i][1] + 1])
        return results
        
    
        
if __name__ == "__main__":
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(Solution().xorQueries(arr, queries))