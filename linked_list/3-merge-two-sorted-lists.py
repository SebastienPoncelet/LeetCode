# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
      return l2 or l1

    if l1.val <= l2.val:
      head = ListNode(l1.val)
      l1 = l1.next
    else:
      head = ListNode(l2.val)
      l2 = l2.next

    current = head

    while l1:
      if not l2:
        current.next = l1
        l1 = l1.next
        current = current.next
      elif l1.val <= l2.val:
        current.next = l1
        l1 = l1.next
        current = current.next
      else:
        current.next = l2
        l2 = l2.next
        current = current.next

    while l2:
      current.next = l2
      l2 = l2.next
      current = current.next

    return head


# PERFORMANCE ACCORDING TO LEETCODE
# Runtime: 28 ms, faster than 98.21% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.2 MB, less than 85.43% of Python3 online submissions for Merge Two Sorted Lists.

# Next challenges:
# - Merge k Sorted Lists
# - Merge Sorted Array
# - Sort List
# - Shortest Word Distance II
# - Add Two Polynomials Represented as Linked Lists
# - Longest Common Subsequence Between Sorted Arrays