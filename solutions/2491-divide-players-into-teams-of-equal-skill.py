# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        total_sum = sum(skill)
        n = len(skill)
        target = total_sum * 2 / n

        hash_map = {}
        for i in skill:
            hash_map[i] = hash_map.get(i, 0) + 1

        result = 0
        visted = set()
        for num in hash_map:
            if num in visted:
                continue
            remainder = target - num
            if num == remainder:
                if hash_map[num] % 2 == 1:
                    return -1
                result += num * num * hash_map[num] // 2
                visted.add(num)
            elif remainder in hash_map:
                if hash_map[num] != hash_map[remainder]:
                    return -1
                result += num * remainder * hash_map[num]
                visted.add(num)
                visted.add(remainder)
            else:
                return -1
            
        return int(result)
    
if __name__ == "__main__":
    s = Solution()
    skill = [3,2,5,1,3,4]
    print(s.dividePlayers(skill))