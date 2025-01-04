# https://leetcode.com/problems/separate-black-and-white-balls/description/
class Solution:
    def minimumSteps(self, s: str) -> int:

        # logic: Iterate right to left and count the number of 0 that have already occurred,
        # whenever you iterate on 1 add that counter to the answer.

        swap_time = 0
        zero_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                zero_count += 1
            if s[i] == '1':
                swap_time += zero_count
        return swap_time

if __name__ == "__main__":
    s = Solution()
    print(s.minimumSteps("101"))  # 1