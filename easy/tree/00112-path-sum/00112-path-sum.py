"""
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""

from collections import deque

class Tree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def has_path_sum(self, root, total):
        if not root:
            return False
        total -= root.val
        if total == 0 and root.left is None and root.right is None:
            return True
        return self.has_path_sum(root.left, total) or self.has_path_sum(root.right, total)

    def test(self):
        test_cases = [
            {"list": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], "total": 22},
            {"list": [1, 2], "total": 1}
        ]
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n{i}. {test_case['list']}, total : {test_case['total']}")
            root = self.list_to_tree(test_case['list'])
            self.print_tree(root)
            res = self.has_path_sum(root, test_case['total'])
            print(f"  - has path sum ? {res}")

    def print_tree(self, root):
        str = []
        self.validate_tree(root, str)
        print(f"  - preorder tree : {str}")

    def validate_tree(self, root, str):
        if not root:
            return "# " 
        str.append(root.val)
        self.validate_tree(root.left, str)
        self.validate_tree(root.right, str)

    def list_to_tree(self, list):
        if not list:
            return None
        q = deque()
        i = 1
        cnt = len(list)
        root = Tree(list[0])
        q.append(root)

        while q and i < cnt:
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

