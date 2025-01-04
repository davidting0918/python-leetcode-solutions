# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06

from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode(0)
        pointer = dummy
        while head:
            if head.val not in num_set:
                pointer.next = head
                pointer = pointer.next
            head = head.next
        pointer.next = None
        return dummy.next
        
