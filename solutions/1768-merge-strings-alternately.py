class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        min_length = min(len(word1), len(word2))
        max_length = max(len(word1), len(word2))
        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])
        
        return "".join(result) + word1[min_length:max_length] + word2[min_length:max_length]
    

if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("ab", "pqrs"))