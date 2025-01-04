# https://leetcode.com/problems/integer-to-english-words/description/?envType=daily-question&envId=2024-08-07
class Solution:
    def numberToWords(self, num: int) -> str:
        def transfer_three_digit(n: int) -> str:

            if n == 0:
                return ""
            elif n < 20:
                return number_map[n]
            elif n < 100:
                ten, below_ten = divmod(n, 10)
                return number_map[ten * 10] + ("" if below_ten == 0 else " " + number_map[below_ten])
            else:
                hundred, below_hundred = divmod(n, 100)
                return f"{number_map[hundred]} Hundred" + ("" if below_hundred == 0 else " " + transfer_three_digit(below_hundred))
            
        number_map = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
            1000000000000: "Trillion"
        }

        if num == 0:  # Can't use `if num in number_map` because if num is 100 then answer should be 'One Hundred' not 'Hundred'
            return number_map[num]
        
        unit = ["", "Thousand", "Million", "Billion", "Trillion"]
        index = 0

        result = []
        while num > 0:
            num, remainder = divmod(num, 1000)
            if remainder > 0:
                result.append(transfer_three_digit(remainder) + ("" if index == 0 else " " + unit[index]))
            index += 1

        return " ".join(result[::-1])
    

if __name__ == "__main__":
    s = Solution()

    num = 123
    print(num)
    print(s.numberToWords(num))

    num = 12345
    print(num)
    print(s.numberToWords(num))