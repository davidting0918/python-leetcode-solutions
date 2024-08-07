# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        step_num = m + n - 2
        
        lower = min(m, n) - 1
        
        result = 1
        for i in range(lower):
            result *= step_num - i
            result /= i + 1
        
        return int(result)
    
if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))