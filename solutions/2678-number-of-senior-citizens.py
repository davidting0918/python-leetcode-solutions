# https://leetcode.com/problems/number-of-senior-citizens/description/
class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11]) * 10 + int(detail[12]) > 60:
                count += 1
        return count
    

if __name__ == "__main__":
    s = Solution()
    details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    print(s.countSeniors(details))