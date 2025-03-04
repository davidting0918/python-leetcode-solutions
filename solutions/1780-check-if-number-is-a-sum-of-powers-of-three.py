# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Use Ternary numeral system, if any digit is 2, meaning it costs 2*3^i,
        # which is not allowed since each number can be used only once.

        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

if __name__ == "__main__":
    s = Solution()
    n = 12
    print(s.checkPowersOfThree(n))