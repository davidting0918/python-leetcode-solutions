# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode(0, head)
        while head.next:
            insertion = self.gcd(head.val, head.next.val)
            temp = head.next
            head.next = ListNode(insertion)
            head.next.next = temp
            head = head.next.next

        return dummy.next

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.gcd(16, 6))