# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/?envType=daily-question&envId=2026-03-29
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        return sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])

if __name__ == '__main__':
    s = Solution()

    # Example 1
    assert s.canBeEqual("abcd", "cdab") == True
    # Example 2
    assert s.canBeEqual("abcd", "dacb") == False

    print("All test cases passed!")
