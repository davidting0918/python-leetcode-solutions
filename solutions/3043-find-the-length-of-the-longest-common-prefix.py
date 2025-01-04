# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(i) for i in arr1]
        arr1_set = {
            arr1[i][:j] for i in range(len(arr1)) for j in range(1, len(arr1[i]) + 1)
        }
        arr2 = sorted([str(i) for i in arr2], reverse=True)

        max_len = 0
        for str2 in arr2:
            for i in range(1, len(str2) + 1):
                if str2[:i] in arr1_set:
                    max_len = max(max_len, i)
                else:
                    break
        return max_len



if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 10, 100]
    arr2 = [1000]
    print(s.longestCommonPrefix(arr1, arr2))
