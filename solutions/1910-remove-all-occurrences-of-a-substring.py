# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        while part in s:
            i = s.index(part)
            s = s[:i] + s[i+n:]
        
        return s
    
if __name__ == "__main__":
    s = Solution()
    string = 'daabcbaabcbc'
    part = 'abc'
    print(s.removeOccurrences(string, part))