# https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19
class Solution:
    def minSteps(self, n: int) -> int:
        result = 0

        start = 2
        while n > 1:
            num, remainder = divmod(n, start)
            if remainder == 0:
                result += start
                n = num
                start = 2
                continue
            start += 1
            
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.minSteps(4))