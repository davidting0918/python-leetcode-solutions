# https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # the answer should have the same number of 1 as num2 and num1 XOR answer should be min
        # since XOR need to be minimized, so the difference need to happen rightmost bit
        # first count the dif in number of 1 between num2 and num1, if num1 > num2, then 1 -> 0, if num1 < num2, then 0 -> 1
        num2_bit_count = bin(num2).count('1')

        num2_bin = bin(num2)[2:]
        num1_bin = bin(num1)[2:]
        print(num1_bin, num2_bin)
        additional_one = num2_bit_count - num1_bin.count('1')
        answer = ["0"] * (additional_one) + [i for i in num1_bin]

        if additional_one == 0:
            return int(answer, 2)
        elif additional_one > 0:
            index = -1
            while additional_one > 0:
                if answer[index] == "0":
                    answer[index] = "1"
                    additional_one -= 1
                index -= 1

        elif additional_one < 0:
            index = -1
            while additional_one < 0:
                if answer[index] == "1":
                    answer[index] = "0"
                    additional_one += 1
                index -= 1

        return int("".join(answer), 2)


if __name__ == "__main__":
    s = Solution()
    num1 = 25
    num2 = 72
    print(s.minimizeXor(num1, num2))  