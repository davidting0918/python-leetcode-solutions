# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ""

        count = 1
        prev = s[0]
        for index in range(1, len(s)):
            if s[index] == prev:
                count += 1
            else:
                count = 1
                prev = s[index]

            if count < 3:
                output += s[index]

        return s[0] + output


if __name__ == "__main__":
    s = Solution()
    string = "llllleeetcode"
    print(s.makeFancyString(string))  # "leetcode"