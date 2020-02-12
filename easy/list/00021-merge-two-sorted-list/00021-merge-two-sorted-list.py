"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Expected Result:
1. [1, 2, 4] & [1, 3, 4]: [1, 1, 2, 3, 4, 4]
2. [1, 4] & [1, 2, 3, 4, 5, 7]: [1, 1, 2, 3, 4, 4, 5, 7]
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge_two_lists(self, l1, l2):
        head = node = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1: node.next = l1
        if l2: node.next = l2

        return head.next


    def list_to_listnode(self, list):
        res = node = ListNode(None)
        for x in list:
            node.next = ListNode(x)
            node = node.next
        return res.next


    def listnode_to_list(self, listnode):
        res = []
        while listnode:
            res.append(listnode.val)
            listnode = listnode.next
        return res


    def test(self):
        test_cases = [
            {"l1": [1,2,4], "l2": [1,3,4]},
            {"l1": [1,4],   "l2": [1,2,3,4,5,7]}
        ]
        for i, test_case in enumerate(test_cases, 1):
            n1, n2 = test_case['l1'], test_case['l2']
            l1, l2 = self.list_to_listnode(n1), self.list_to_listnode(n2)
            res    = self.merge_two_lists(l1, l2)
            lnode  = self.listnode_to_list(res)
            print(f"{i}. {n1} & {n2}: {lnode}")


if __name__ == '__main__':
    Solution().test()

