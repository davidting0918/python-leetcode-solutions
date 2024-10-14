# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/?envType=daily-question&envId=2024-10-13
from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float('-inf')

        # 將每個列表的第一個元素加入堆中
        for i, num_list in enumerate(nums):
            if num_list:
                heapq.heappush(heap, (num_list[0], i, 0))
                max_val = max(max_val, num_list[0])

        # 初始化結果範圍
        result = [float('-inf'), float('inf')]

        # 主循環
        while len(heap) == len(nums):
            min_val, list_index, element_index = heapq.heappop(heap)

            # 更新結果範圍
            if max_val - min_val < result[1] - result[0]:
                result = [min_val, max_val]

            # 如果當前列表還有下一個元素，將其加入堆中
            if element_index + 1 < len(nums[list_index]):
                next_val = nums[list_index][element_index + 1]
                heapq.heappush(heap, (next_val, list_index, element_index + 1))
                max_val = max(max_val, next_val)

        return result

if __name__ == "__main__":
    s = Solution()
    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    print(s.smallestRange(nums))  # [20,24]