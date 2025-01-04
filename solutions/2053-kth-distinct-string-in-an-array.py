# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=daily-question&envId=2024-08-05
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        distinct = []
        remove = []
        for i in arr:
            if i not in distinct and i not in remove:
                distinct.append(i)
            elif i in distinct:
                distinct.remove(i)
                remove.append(i)

        return distinct[k - 1] if k <= len(distinct) else ""
    
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ht = {}

        for i in arr:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        
        for i in ht:
            if ht[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""