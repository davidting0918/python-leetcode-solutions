# https://leetcode.com/problems/tuple-with-same-product/description/?envType=daily-question&envId=2025-02-06

from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        product_dict = {}
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                product_dict[product] = product_dict.get(product, 0) + 1

        answer = 0
        for key in product_dict:
            count = product_dict[key]
            if count >= 2:
                answer += count * (count-1) * 4
        return answer
    
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,4,5,10]
    print(s.tupleSameProduct(nums))