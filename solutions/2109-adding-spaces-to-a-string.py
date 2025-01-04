# https://leetcode.com/problems/adding-spaces-to-a-string/description/
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        spaces.append(len(s))
        spaces.append(0)
        spaces.sort()

        for i in range(1, len(spaces)):
            output += f"{s[spaces[i-1]:spaces[i]]} "
        return output[:-1]

if __name__ == "__main__":
    s = Solution()
    string = "LeetcodeHelpsMeLearn"
    spaces = [8,13,15]
    print(s.addSpaces(string, spaces))