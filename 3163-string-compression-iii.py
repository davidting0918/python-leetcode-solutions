# https://leetcode.com/problems/string-compression-iii/description/?envType=daily-question&envId=2024-11-04
class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)

        count = 1
        current = word[0]
        if n == 1:
            return f"{count}{current}"

        compressed = ""
        for i in range(1, n):
            if word[i] == current:
                if count == 9:
                    compressed += f"{count}{current}"
                    current = word[i]
                    count = 0
                count += 1

                if i == n - 1:
                    compressed += f"{count}{current}"
                continue
            else:
                compressed += f"{count}{current}"
                current = word[i]
                count = 1
                if i == n - 1:
                    compressed += f"{count}{current}"
                continue


        return compressed
    
if __name__ == "__main__":
    s = Solution()
    word = "d"
    print(s.compressedString(word))