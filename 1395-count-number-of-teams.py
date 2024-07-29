# https://leetcode.com/problems/count-number-of-teams/description/
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
    
