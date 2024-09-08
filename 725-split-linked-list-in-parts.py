# https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2024-09-08
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [
            ListNode() for _ in range(k)
        ]

        index = 0
        while head:
            result[index].next = head
            head = head.next
            result[index] = result[index].next
            index = (index + 1) % k

        return [node.next for node in result]

