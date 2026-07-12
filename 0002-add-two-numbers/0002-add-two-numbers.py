# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        rs = ListNode() 
        temp = rs 
        carry = 0
        while  l1 and  l2:
            cur = l1.val + l2.val + carry
            temp.next= ListNode(cur % 10)
            carry = cur // 10
            temp = temp.next
            l1 = l1.next 
            l2 = l2.next 
        while l1:
            cur = l1.val + carry
            temp.next= ListNode(cur % 10)
            carry = cur // 10
            temp = temp.next
            l1 = l1.next 
        while l2:
            cur = l2.val + carry
            temp.next= ListNode(cur % 10)
            carry = cur // 10
            temp = temp.next
            l2 = l2.next
                 
        if carry:
            temp.next= ListNode(carry)
               
        return rs.next    