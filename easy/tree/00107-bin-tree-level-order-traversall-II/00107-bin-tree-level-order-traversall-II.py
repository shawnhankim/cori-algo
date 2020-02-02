"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""

from collections import deque, defaultdict

class Tree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def level_order_bottom(self, root):
        if not root:
            return None

        q = deque()
        q.append(root)
        res = []

        while q:
            temp = []
            node_cnt = len(q)
            while node_cnt > 0:
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                   q.append(node.left)
                if node.right:
                   q.append(node.right)
                node_cnt -= 1
            res.append(temp)
        return res[::-1]

    def level_order_bottom2(self, root):
        if not root:
            return None

        q = deque()
        d = defaultdict(list)
        depth = 0
        q.append((root, depth))
       
        while q:
            node, depth = q.popleft()
            d[depth].append(node.val)

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

        res = []
        for key, value in d.items():
            res.append(value)
        return res[::-1]

    def level_order_bottom1(self, root):
        if not root:
            return None

        o = 0        # old depth
        d = 0        # depth
        q = deque()  # queue
        q.append((root, d))

        s = []       # stack
        l = []       # list

        while q:
            node, d = q.popleft()

            if o != d:
                s.append(l)
                l = []
                o = d

            l.append(node.val)

            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))

        if l:
            s.append(l)

        res = []
        while s:
            res.append(s.pop())
        return res

    def test(self):
        test_cases = [
            [3, 9, 20, None, None, 15, 7],
            [3, 1, 2]
        ]
        for i, test_case in enumerate(test_cases, 1):
            root = self.list_to_tree(test_case)
            #self.print_root(root)
            res = self.level_order_bottom(root)
            print(f"\n{i}. test case : {test_case}")
            print(f"   - result : {res}")

    def print_root(self, root):
        str = self.print_helper(root)
        print(f"root : {str}")
       
    def print_helper(self, root):
        if not root:
            return ""
        str = f"{root.val} "
        return str + (self.print_helper(root.left) + self.print_helper(root.right))

    def list_to_tree(self, list):
        if not list:
            return None
        i = 0 
        q = deque()
        l = len(list)

        root = Tree(list[0])
        q.append(root)

        while q:
            node = q.popleft()
            
            i += 1
            if i < l and list[i]:
                node.left = Tree(list[i])
                q.append(node.left)
            
            i += 1
            if i < l and list[i]:
                node.right = Tree(list[i])
                q.append(node.right)
        return root

def main():
    Solution().test()

if __name__ == '__main__':
    main()

