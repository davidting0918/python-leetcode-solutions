# https://leetcode.com/problems/integer-to-roman/description/
class Solution:
    def intToRoman(self, num: int) -> str:
        ht = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        result = ""

        for i in sorted(ht.keys(), reverse=True):
            while num >= i:
                result += ht[i]
                num -= i
            continue


        return result
    
if __name__ == "__main__":
    s = Solution()

    num = 1099
    print(num)
    print(s.intToRoman(num))
