# https://leetcode.com/problems/pascals-triangle/description/
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        results = [[1]]
        for i in range(1, numRows):
            results.append(self.generateRow(results[i-1]))
        return results
    
    def generateRow(self, row: List[int]) -> List[int]:
        newRow = [1]
        for i in range(1, len(row)):
            newRow.append(row[i-1] + row[i])
        newRow.append(1)
        return newRow
    


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]