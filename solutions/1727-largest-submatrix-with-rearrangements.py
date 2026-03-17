from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
                else:
                    matrix[i][j] = 0

        ans = 0
        for i in range(m):
            row = sorted(matrix[i], reverse=True)  # in descending order
            for j in range(n):
                ans = max(ans, row[j] * (j + 1))
                print(f"row: {row}, j: {j}, ans: {ans}")


        return ans



if __name__ == "__main__":
    s = Solution()
    matrix = [[0,0,1],[1,1,1],[1,0,1]]
    print(s.largestSubmatrix(matrix))