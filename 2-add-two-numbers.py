# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        l1_num = self.convert(l1)
        l2_num = self.convert(l2)
        total = l1_num + l2_num
        return self.convert_to_listnode(total)
    
    def convert_to_listnode(self, num: int) -> list[ListNode]:
        num_str = str(num)[::-1]
        result = ListNode(int(num_str[0]))

        current = result
        for digit in num_str[1:]:
            current.next = ListNode(int(digit))
            current = current.next
        return result
        

    def convert(self, listnode: list[ListNode]) -> int:
        num = 0
        index = 0
        while listnode:
            num += listnode.val * 10 ** index
            index += 1
            listnode = listnode.next
        return num

