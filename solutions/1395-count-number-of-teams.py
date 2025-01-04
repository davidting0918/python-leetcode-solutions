# https://leetcode.com/problems/count-number-of-teams/description/
import bisect
class Solution:
    def numTeams_on3(self, rating: list[int]) -> int:
        count = 0
        for first in range(len(rating)):
            for second in range(first + 1, len(rating)):
                for third in range(second + 1, len(rating)):
                    if rating[first] < rating[second] < rating[third] or rating[first] > rating[second] > rating[third]:
                        count += 1
        return count
    
    def numTeams_on2(self, rating: list[int]) -> int:
        count = 0
        for i in range(1, len(rating) - 1):
            left_less, left_more = 0, 0
            right_less, right_more = 0, 0
            for j in range(i):
                if rating[j] < rating[i]:
                    left_less += 1
                else:
                    left_more += 1
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    right_less += 1
                else:
                    right_more += 1
            count += left_less * right_more + left_more * right_less
        return count
    
    def numTeams_on1(self, rating: list[int]) -> int:
        count = 0

        l = []
        sorted_rating = sorted(rating)
        low = {r: i for i, r in enumerate(sorted_rating)}
        
        n = len(rating)

        for idx, r in enumerate(rating):
            i = bisect.bisect(l, r)
            l.insert(i, r)
            j = low[r] - i
            count += i * (n - 1 - idx - j) + j * (idx - i)  # asc + desc

            print(f"Original index: {idx}, rating: {r}, bisect index: {i}, low index: {low[r]}, "
                  f"{i} * ({n} - 1 - {idx} - {j}) + {j} * ({idx} - {i}) = {i * (n - 1 - idx - j) + j * (idx - i)}, "
                  f"current_num: {i * (n - 1 - idx - j) + j * (idx - i)}, total: {count}")
            
        return count
    
if __name__ == "__main__":
    s = Solution()
    ratings = [2,5,3,4,1]
    print(ratings)
    s.numTeams_on1(ratings)

    ratings = [1,2,3,4]
    print(ratings)
    s.numTeams_on1(ratings)
