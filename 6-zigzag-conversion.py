# https://leetcode.com/problems/zigzag-conversion/description/
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        results = {
            i: [] for i in range(numRows)
        }
        
        num_per_group = 2 * numRows - 2

        for start in range(0, len(s), num_per_group):
            sub_string = s[start:start + num_per_group]
            print(f"Start: {start}, sub_string: {sub_string}")
        return
    
if __name__ == "__main__":
    s = Solution()
    string = "PAYPALISHIRING"
    print(s.convert(string, 3))