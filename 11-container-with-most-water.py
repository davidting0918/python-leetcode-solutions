# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = max(area, max_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
    
if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))