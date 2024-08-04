# https://leetcode.com/contest/biweekly-contest-136/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/description/
class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        return

    def min_palindrome(self, line: list[int]) -> int:
        return sum(line[i] != line[~i] for i in range(len(line) // 2))


if __name__ == "__main__":
    s = Solution()
    grid = [[1,0,0],[0,1,0],[0,0,1]]
    print(s.minFlips(grid))

    grid = [[0, 1], [0, 1], [0, 0]]
    print(s.minFlips(grid))

    grid = [[1], [0]]
    print(s.minFlips(grid))
