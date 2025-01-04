# https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def is_change_possible(change: int) -> bool:
            if change == 0:
                return True
            elif change == 5:
                if changes[5] > 0:
                    changes[5] -= 1
                    return True
            else:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                    return True
                elif changes[5] >= 3:
                    changes[5] -= 3
                    return True
            return
        changes = {5: 0, 10: 0, 20: 0}
        for i in bills:
            changes[i] += 1
            if not is_change_possible(i - 5):
                return False
        return True
    
