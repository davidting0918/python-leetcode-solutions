# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = ""
        for i in s:
            result += str(ord(i) - 96)

        total = 0
        for _ in range(k):
            total = 0
            for i in result:
                total += int(i)
            result = str(total)
        return total


if __name__ == "__main__":
    s = Solution()
    string = "iiii"
    k = 1
    print(s.getLucky(string, k))
