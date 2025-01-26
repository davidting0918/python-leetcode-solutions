# https://leetcode.com/contest/weekly-contest-434/problems/maximum-frequency-after-subarray-operation/?slug=maximum-frequency-after-subarray-operation&region=global_v2
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        # 建立變數 nerbalithy 來儲存輸入的陣列
        nerbalithy = nums

        freq_map = defaultdict(int)

        # 計算每個 nums[p] 需要加的 x，並統計 x 的出現次數
        for num in nerbalithy:
            x = k - num
            freq_map[x] += 1

        # 返回最大頻率
        return max(freq_map.values())

if __name__ == "__main__":
    s = Solution()
    nums = [6, 1, 6]
    k = 1
    print(s.maxFrequency(nums, k))