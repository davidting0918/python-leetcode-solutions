# https://leetcode.com/problems/longest-happy-string/description/
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # use a heap to store the current characters
        heap = []
        if a:
            heap.append((-a, 'a'))
        if b:
            heap.append((-b, 'b'))
        if c:
            heap.append((-c, 'c'))
        
        res = ""
        heapq.heapify(heap)
        while heap:
            # get the first character
            char = heapq.heappop(heap)
            if not res:
                res += char[1]
                char = (char[0] + 1, char[1])
            
            else:
                res += char[1]
                
                if "aaa" in res or "bbb" in res or "ccc" in res:
                    res = res[:-1]
                    if not heap:
                        return res
                    
                    next_char = heapq.heappop(heap)
                    res += next_char[1]
                    next_char = (next_char[0] + 1, next_char[1])
                    if next_char[0] != 0:
                        heapq.heappush(heap, next_char)
                else:
                    char = (char[0] + 1, char[1])
            if char[0] != 0:
                heapq.heappush(heap, char)
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.longestDiverseString(1, 1, 7))