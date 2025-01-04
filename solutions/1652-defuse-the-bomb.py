# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k > 0: 
            d_list = code + code
        else:
            d_list = code[k-1:] + code[:k-1] + code[k-1:] + code[:k-1]
        n = len(code)
        output = []
        k = abs(k)
        for i in range(n):
            output.append(
                sum(d_list[i+1:i+k+1])
            )    
        return output
    
if __name__ == "__main__":
    s = Solution()
    nums = [2,4,9,3]
    k = -2
    print(s.decrypt(nums, k))  # [12,5,6,13]
