"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Expected Result:

1. [1, 1, 2] -> [1, 2]
2. [1, 1, 2, 3, 3] -> [1, 2, 3]
"""

class ListNode:
    def __init__(self, x):
        self.val  = x
        self.next = None


class Solution(object):
    def delete_duplicates(self, head):
        dummy = head
        while head and head.next:
            if head.val == head.next.val:
                temp      = head.next
                head.next = head.next.next
                temp      = None
            else:
                head      = head.next
        return dummy.next
             

    def nums_to_listnode(self, nums):
        res = node = ListNode(None)
        for n in nums:
            node.next = ListNode(n)
            node = node.next            
        return res


    def listnode_to_nums(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res


    def test(self):
        test_cases = [
            [1,1,2],
            [1,1,2,3,3]
        ]
        for i, nums in enumerate(test_cases, 1):
            head = self.nums_to_listnode(nums)
            node = self.delete_duplicates(head)
            list = self.listnode_to_nums(node)
            print(f"{i}. {nums} -> {list}")


if __name__ == '__main__':
    Solution().test()

