# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # use two pointer method
        p1 = 0
        p2 = 0
        n1 = len(str1)
        n2 = len(str2)

        while p1 < n1 and p2 < n2:
            candidate = [
                ord(str1[p1]),
                ord(str1[p1]) + 1 if ord(str1[p1]) != 122 else 97,
            ]
            str2_no = ord(str2[p2])
            if str2_no in candidate:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
            continue
        if p2 == n2:
            return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    str1 = "zc"
    str2 = "ad"
    print(s.canMakeSubsequence(str1, str2))  # True