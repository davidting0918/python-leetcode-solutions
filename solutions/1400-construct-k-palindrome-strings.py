# https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-11
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        hash_table = {}

        for char in set(s):
            hash_table[char] = s.count(char)

        odd_count = 0
        for i in hash_table.values():
            if i % 2 != 0:
                odd_count += 1

        return True if odd_count <= k else False

if __name__ == '__main__':
    s = Solution()
    string = 'annabelle'
    k = 2
    print(s.canConstruct(string, k)) # True