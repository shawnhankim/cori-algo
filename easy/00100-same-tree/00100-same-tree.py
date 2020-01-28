"""
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def is_sametree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype : bool
        """
        if p == None and q == None:
            return True
        if (p != None and q == None) or (p == None and q != None) or (p.val != q.val):
            return False
        return self.is_sametree(p.left, q.left) and self.is_sametree(p.right, q.right)

    def string_to_treenode(self, inputs):
        input = input.strip()
        input = input[1:-1]
        if not input:
            return None

        inputs = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputs[0]))
        node_q = [root]
        front = 0
        idx   = 1
        while idx < len(inputs):
            node = node_q[front]
            front += 1

            item = inputs[idx]
            idx += 1
            if item != "null":
                left_num = int(item)
                node.left = TreeNode(left_num)
                node_q.append(node.left)

            if idx >= len(inputs):
                break

            item = inputs[idx]
            idx += 1
            if item != "null":
                right_num = int(item)
                node.right = TreeNode(right_num)
                node_q.append(node.right)
        return root
    
    def list_to_treenode(self, inputs):
        from collections import deque
        root = TreeNode(inputs[0])
        q = deque()
        q.append(root)
        toggle = 0
        cnt = len(inputs)
        for num in inputs:
            node = q.popleft()
            new_node = TreeNode(num)
            if not toggle:
                node.left = new_node
            else:
                node.right = new_node
            toggle ^= 1
            q.append(new_node)
        return root

def main():
    test_cases = [
        { "p": [1,2,3], "q": [1,2,3] },
        { "p": [1,2],   "q": [1,None,2] },
        { "p": [1,2,1], "q": [1,1,2] }
    ]
    sol = Solution()
    for i, test_case in enumerate(test_cases, 1):
        p = sol.list_to_treenode(test_case["p"])
        q = sol.list_to_treenode(test_case["q"])
        res = sol.is_sametree(p, q)
        print(f"{i}. {test_case} are same tree : {res}")

if __name__ == '__main__':
    main()

