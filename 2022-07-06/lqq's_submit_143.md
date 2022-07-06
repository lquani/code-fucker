## 题目
https://leetcode.cn/problems/reorder-list/submissions/
## 思路
链表中位数，链表反转，链表合并三道题的结合体
## code
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        left = head 
        right = slow.next 
        slow.next = None 

        reverse = right 
        res = None 
        while reverse:
            cur = reverse.next
            reverse.next = res 
            res = reverse 
            reverse = cur
        right = res 
        while left and right:
            l = left.next 
            r = right.next 
            left.next = right 
            left = l 
            right.next=left 
            right = r```
