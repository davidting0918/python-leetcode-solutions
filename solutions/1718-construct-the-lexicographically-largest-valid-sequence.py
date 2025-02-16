# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/?envType=daily-question&envId=2025-02-16
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        total_length = 2 * n - 1

        answer = [0] * total_length

        for num in range(n, 1, -1):
            for i in range(2 * n - 1):
                if answer[i] == 0:
                    next_index = i + num
                    if next_index >= total_length:
                        break
                    if answer[next_index] == 0:
                        answer[i] = num
                        answer[next_index] = num
                        break

        return [i if i != 0 else 1 for i in answer]

if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.constructDistancedSequence(n))