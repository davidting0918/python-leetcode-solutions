# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_set = set()
        for right, string in enumerate(s):
            while string in char_set:
                max_length = max(max_length, right - left)
                char_set.remove(s[left])
                left += 1
                
            char_set.add(string)

            print(f"Char set: {char_set}, left: {left}, right: {right}, max_length: {max_length}")

        return max(max_length, len(s) - left)
    
if __name__ == "__main__":
    s = Solution()
    string = "dvdf"
    print(s.lengthOfLongestSubstring(string))

    string = "abcabcbb"
    print(s.lengthOfLongestSubstring(string))