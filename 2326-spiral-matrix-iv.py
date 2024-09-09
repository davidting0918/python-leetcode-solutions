# https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        outputs = [
            [-1] * n for _ in range(m)
        ]

        x, y = 0, 0
        index = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while head:
            outputs[x][y] = head.val
            head = head.next

            dx, dy = directions[index]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= m or ny < 0 or ny >= n or outputs[nx][ny] != -1:
                index = (index + 1) % 4
                dx, dy = directions[index]
                nx, ny = x + dx, y + dy

            x, y = nx, ny

        return outputs