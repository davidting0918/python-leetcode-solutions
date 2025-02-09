# https://leetcode.com/contest/weekly-contest-436/problems/assign-elements-to-groups-with-constraints/?slug=sort-matrix-by-diagonals&region=global_v2
from typing import List
import math

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        hash_table = {}

        for i, val in enumerate(elements):
            if val not in hash_table:
                hash_table[val] = i

        answers = []
        for num in groups:
            min_index = float('inf')
            sqrt_num = int(math.sqrt(num))

            for i in range(1, sqrt_num+1):
                if num % i == 0:
                    if i in hash_table:
                        min_index = min(min_index, hash_table[i])
                    if num // i in hash_table:
                        min_index = min(min_index, hash_table[num // i])
            answers.append(
                -1 if min_index == float('inf') else min_index
            )
        return answers


if __name__ == "__main__":
    s = Solution()
    groups = [8,4,3,2,4]
    elements = [4,2]
    print(s.assignElements(groups, elements)) # [4, 2]