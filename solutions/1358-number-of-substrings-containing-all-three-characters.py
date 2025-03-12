# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2025-03-11
import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length = len(s)
        a_index = []
        b_index = []
        c_index = []

        for i in range(length):
            if s[i] == 'a':
                a_index.append(i)
            elif s[i] == 'b':
                b_index.append(i)
            elif s[i] == 'c':
                c_index.append(i)

        answer = 0
        for start in range(length):
            a = -1
            b = -1
            c = -1
            
            # Use binary search to find first index >= start
            a_pos = bisect.bisect_left(a_index, start)
            b_pos = bisect.bisect_left(b_index, start)
            c_pos = bisect.bisect_left(c_index, start)
            
            if (a_pos < len(a_index) and 
                b_pos < len(b_index) and 
                c_pos < len(c_index)):
                a = a_index[a_pos]
                b = b_index[b_pos] 
                c = c_index[c_pos]
                answer += length - max(a, b, c)

        return answer
    
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubstrings("abcabc"))
