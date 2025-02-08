# https://leetcode.com/problems/design-a-number-container-system/description/

import collections
from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.nums = {}  # key: index, value: num
        self.index = collections.defaultdict(SortedSet)  # key: num, index: heap of index

    def change(self, index: int, number: int) -> None:
        if index in self.nums:
            old_num = self.nums[index]
            self.index[old_num].remove(index)
            if not self.index[old_num]:
                del self.index[old_num]

        self.nums[index] = number
        self.index[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.index or not self.index[number]:
            return -1
        else:
            return self.index[number][0]

if __name__ == "__main__":
    s = NumberContainers()
    actions = ["find","change","change","change","change","find","change","find"]
    values = [[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]

    for i, action in enumerate(actions):
        if action == "find":
            print(s.find(values[i][0]))
        else:
            print(s.change(values[i][0], values[i][1]))
