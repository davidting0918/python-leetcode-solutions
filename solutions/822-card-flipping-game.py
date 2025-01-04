# https://leetcode.com/problems/card-flipping-game/description/
from typing import List
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        Logic is using set() to store the unique values of the cards that can be flipped,
        if back and front are the same meaning even if we flip the card, it will still appear in each side
        """
        results = set()
        exclude = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                exclude.add(fronts[i])
                results.discard(fronts[i])
            else:
                if fronts[i] not in exclude:
                    results.add(fronts[i])
                if backs[i] not in exclude:
                    results.add(backs[i])

        return min(results) if results else 0

    def flipgame_v2(self, fronts: List[int], backs: List[int]) -> int:
        """
        Logic is using both set() to exclude the cards that can't be flipped and store the unique values of the cards that can be flipped.

        """
        both = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                both.add(fronts[i])

        front = set(fronts)
        back = set(backs)
        all_number = front | back

        one_side_nums = all_number - both
        return min(one_side_nums) if one_side_nums else 0


if __name__ == "__main__":
    s = Solution()
    fronts = [1,2,4,4,7]
    backs = [1,3,4,1,3]
    print(s.flipgame(fronts, backs))