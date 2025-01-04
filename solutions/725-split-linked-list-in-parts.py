# https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2024-09-08
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        width, remainder = divmod(n, k)

        results = [None] * k

        curr, index = head, 0

        while curr and index < k:
            results[index] = curr

            length = width + (1 if remainder > 0 else 0)

            for _ in range(length - 1):
                if curr:
                    curr = curr.next

            if curr:
                curr.next, curr = None, curr.next

            index += 1
            remainder -= 1
        return results
