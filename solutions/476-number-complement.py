# https://leetcode.com/problems/number-complement/description/
class Solution:
    def findComplement(self, num: int) -> int:
        
        for i in range(32):
            if 2 ** i > num:
                return 2 ** i - 1 - num
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findComplement(5))