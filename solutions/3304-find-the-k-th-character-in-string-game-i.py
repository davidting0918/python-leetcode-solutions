# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=daily-question&envId=2025-07-03
class Solution:
    def kthCharacter(self, k: int) -> str:
        string = "1"
        while len(string) < k:
            string += self.next_string(string)
        return chr(int(string[k - 1]) + 96)
    
    def next_string(self, string: str) -> str:
        result = ""
        for s in string:
            result += str(int(s) + 1)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.kthCharacter(5))