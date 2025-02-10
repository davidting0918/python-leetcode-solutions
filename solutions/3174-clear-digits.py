# https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10

class Solution:
    def clearDigits(self, s: str) -> str:
        
        numbers_string = "0123456789"

        letters = []

        for i in s:
            if i in numbers_string:
                if letters:
                    letters.pop()
            else:
                letters.append(i)
        return "".join(letters)
    
if __name__ == "__main__":
    s = Solution()
    string = 'abc'
    print(s.clearDigits(string))