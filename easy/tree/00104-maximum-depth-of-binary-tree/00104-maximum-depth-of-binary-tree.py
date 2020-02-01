"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""
from collections import deque

class Tree(object):
    def __init__(self, x):
        self.val = x
        self.left = 0
        self.right = 0

class Solution(object):
    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

    def test(self):
        test_cases = [
            [3, 9, 20, None, None, 15, 7],
            [3, 1, 2],
            [3, 1, None]
        ]
        for i, test_case in enumerate(test_cases, 1):
            root = self.list_to_tree(test_case)
            res = self.max_depth(root)
            print(f"{i}. max depth : {res} for {test_case}")

    def list_to_tree(self, list):
        if not list:
            return None
        
        root = Tree(list[0])
        q = deque()
        q.append(root)
        i = 1
        cnt = len(list)
        while q:
            node = q.popleft()
            if i < cnt and list[i]:
                node.left = Tree(list[i])
                q.append(node.left)
            i += 1

            if i < cnt and list[i]:
                node.right = Tree(list[i])
                q.append(node.right)
            i += 1

        return root

def main():
    Solution().test()

if __name__ == '__main__':
    main()

