class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base36(num: int) -> str:
            if num == 0:
                return "0"
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while num > 0:
                result = digits[num % 36] + result
                num //= 36
            return result

        hex_part = hex(n * n)[2:].upper()         # n² 的十六進位表示（去掉 "0x" 並轉大寫）
        base36_part = to_base36(n * n * n)        # n³ 的三十六進位表示
        return hex_part + base36_part             # 串接兩者

    
if __name__ == "__main__":
    solution = Solution()
    print(solution.concatHex36(13))