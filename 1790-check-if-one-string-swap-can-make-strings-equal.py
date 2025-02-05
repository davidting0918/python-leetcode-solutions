# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if set(s1) != set(s2):
            return False
        
        if len(s1) != len(s2):
            return False

        dif_count = 0
        n = len(s1)

        for i in range(n):
            if s1.count(s1[i]) != s2.count(s1[i]):
                return False

            if s1[i] != s2[i]:
                dif_count += 1
        return dif_count <= 2
    

if __name__ == '__main__':
    s = Solution()
    s1 = "attack"
    s2 = "defend"
    print(s.areAlmostEqual(s1, s2))