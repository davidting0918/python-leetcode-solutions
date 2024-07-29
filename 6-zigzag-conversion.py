# https://leetcode.com/problems/zigzag-conversion/description/
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        results = {
            i: [] for i in range(numRows)
        }
        
        num_per_group = 2 * numRows - 2
        palindrome_index = self.create_palindrome_index(numRows)

        for index, char in enumerate(s):
            group_index = index % num_per_group
            results[palindrome_index[group_index] - 1].append(char)

        return "".join(["".join(results[i]) for i in results])

    def create_palindrome_index(self, length: int) -> list:
        raw = [i for i in range(1, length + 1)]
        raw += raw[-2:0:-1]
        return raw


if __name__ == "__main__":
    s = Solution()
    string = "PAYPALISHIRING"
    print(s.convert(string, 3))