# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/?envType=daily-question&envId=2024-11-20
import math
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s.count("a") < k or s.count("b") < k or s.count("c") < k:
            return -1

        n = len(s)

        for left in range(n//2):
            output = {"a": 0, "b": 0, "c": 0}
            for right in range(1, n//2+1):
                print(left, right)

        return

    def check(self, output: dict, k: int) -> bool:
        for key in output:
            if output[key] < k:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    string = "aabaaaacaabc"
    k = 2
    print(s.takeCharacters(string, k))  # 8
