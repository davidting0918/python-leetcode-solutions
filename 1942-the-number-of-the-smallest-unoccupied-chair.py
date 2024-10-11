# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i, (start, end) in enumerate(times):
            events.append((start, 1, i))
            events.append((end, -1, i))
        events.sort()

        chairs = list(range(len(times)))
        chair_index = {}

        for i in range(len(events)):
            event = events[i]
            if event[1] == 1:
                chairs.sort()
                if event[2] == targetFriend:
                    return chairs[0]
                chair_index[event[2]] = chairs.pop(0)
            else:
                chairs.append(chair_index[event[2]])



if __name__ == '__main__':
    s = Solution()
    times = [[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
    targetFriend = 6
    print(s.smallestChair(times, targetFriend))