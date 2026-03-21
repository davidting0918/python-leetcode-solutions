# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_index = {}
        for right, string in enumerate(s):

            if string in char_index and char_index[string] >= left:
                left = char_index[string] + 1

            max_length = max(max_length, right - left + 1)
            char_index[string] = right

        return max_length
    
if __name__ == "__main__":
    s = Solution()
    string = "dvdf"
    print(s.lengthOfLongestSubstring(string))

    string = "abcabcbb"
    print(s.lengthOfLongestSubstring(string))