# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
class Solution:
    def minimumDeletions(self, s: str) -> int:
        if "a" not in s or "b" not in s:
            return 0
        
        prefix_b = [0] * len(s)
        suffix_a = [0] * len(s)

        count_a = 0
        count_b = 0
        for index_a, index_b in zip(range(len(s) - 1, -1, -1), range(len(s))):
            if s[index_a] == "a":
                count_a += 1
            
            if s[index_b] == "b":
                count_b += 1
            
            prefix_b[index_b] = count_b
            suffix_a[index_a] = count_a
        
        return min([a + b - 1 for a, b in zip(suffix_a, prefix_b) if a != 0 and b != 0])
    
    def minimumDeletions_v2(self, s: str) -> int:
        # if a "a" appear behind a "b", then it can be offset by deleting the "a" so the count_b can be reduced
        min_deletion = 0
        count_b = 0
        for char in s:
            if char == 'b':
                count_b += 1
            elif count_b > 0:
                count_b -= 1
                min_deletion += 1
        return min_deletion


if __name__ == "__main__":
    s = Solution()

    string = "aaaaaa"
    print(string, s.minimumDeletions(string))

    string = "aababbab"
    print(string, s.minimumDeletions(string))

    string = "bbaaaaabb"
    print(string, s.minimumDeletions(string))

    string = "bbababa"
    print(string, s.minimumDeletions(string))

    string = "bbaabab"
    print(string, s.minimumDeletions(string))