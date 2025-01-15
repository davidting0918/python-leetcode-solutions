# https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # the answer should have the same 1 bits as num2 and num1 XOR answer should be min
        num2_bit_count = bin(num2).count('1')

        num1_bin = bin(num1)[2:]
        additional_one = max(0, num2_bit_count - num1_bin.count('1'))
        return


if __name__ == "__main__":
    s = Solution()
    num1 = 3
    num2 = 5
    print(s.minimizeXor(num1, num2))  