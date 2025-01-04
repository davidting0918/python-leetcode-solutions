# https://leetcode.com/problems/jump-game-ii/description/
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
            continue
        return jumps

if __name__ == "__main__":
    s = Solution()

    nums = [2,3,0,1,4]
    print(nums)
    print(s.jump(nums))

    nums = [1, 2, 1, 1, 1]
    print(nums)
    print(s.jump(nums))

    nums = [2,3,1]
    print(nums)
    print(s.jump(nums))

    nums = [1,1,2,1,1]
    print(nums)
    print(s.jump(nums))