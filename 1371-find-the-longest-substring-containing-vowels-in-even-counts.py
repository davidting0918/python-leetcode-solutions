# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        variable purpose:
        1. prefix_mask: use to record the current substring vowel condition and each vowel represent a bit
        2. mask_index_map: use to record the first index of the same prefix_mask, if encounter the same prefix_mask, then the length of the substring is i - mask_index_map[prefix_mask]
        """
        vowel_indices = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        prefix_mask = 0
        mask_index_map = {0: -1}
        max_length = 0
        
        for i, char in enumerate(s):
            if char in vowel_indices:
                prefix_mask ^= (1 << vowel_indices[char])
            
            if prefix_mask in mask_index_map:
                max_length = max(max_length, i - mask_index_map[prefix_mask])
            else:
                mask_index_map[prefix_mask] = i
        
        return max_length
    
if __name__ == "__main__":
    s = Solution()
    print(s.findTheLongestSubstring("eleetminicoworoep"))  # 13