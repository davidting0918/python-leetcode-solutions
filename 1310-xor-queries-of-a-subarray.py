# https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=daily-question&envId=2024-09-13
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = [0 for _ in range(len(queries))]
        
        values = {
        
        }
        
        for i in range(len(queries)):
            if tuple(queries[i]) in values:
                result[i] = values[tuple(queries[i])]
                continue
            if queries[i][0] == queries[i][1]:
                result[i] = arr[queries[i][0]]
                continue
            for j in range(queries[i][0], queries[i][1] + 1):
                result[i] ^= arr[j]
            
            values[tuple(queries[i])] = result[i]
        return result
        
        
    
        
if __name__ == "__main__":
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(Solution().xorQueries(arr, queries))