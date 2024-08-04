# https://leetcode.com/contest/biweekly-contest-136/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description/
class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        # row palindrome
        row_palindrome = 0
        for row in grid:
            row_palindrome += self.min_palindrome(row)


        # column palindrome
        column_palindrome = 0
        for idx in range(len(grid[0])):
            column_palindrome += self.min_palindrome([row[idx] for row in grid])
        return min(row_palindrome, column_palindrome)

    def min_palindrome(self, row: list[int]) -> int:
        # return the min flip to make the row palindrome
        n = len(row)
        left = row[:n//2]
        right = row[n//2:][::-1]

        result = 0
        for l, r in zip(left, right):
            if l != r:
                result += 1

        return result


if __name__ == "__main__":
    s = Solution()
    grid = [[1,0,0],[0,0,0],[0,0,1]]
    print(s.minFlips(grid))

    grid = [[0, 1], [0, 1], [0, 0]]
    print(s.minFlips(grid))

    grid = [[1], [0]]
    print(s.minFlips(grid))