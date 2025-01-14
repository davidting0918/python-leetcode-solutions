# https://leetcode.com/problems/minimum-length-of-string-after-operations/?envType=daily-question&envId=2025-01-13

class Solution:
    def minimumLength(self, s: str) -> int:
        answer = 0

        for letter in set(s):
            letter_num = s.count(letter)
            
            if letter_num % 2 == 0:
                answer += 2
            else:
                answer += 1
                
        return answer
    

if __name__ == "__main__":
    s = Solution()
    string = "abaacbcbb"
    print(s.minimumLength(string)) # 3
