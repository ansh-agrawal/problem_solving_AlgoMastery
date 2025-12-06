"""
Task 64: Invert Binary Tree

Given the root of a binary tree, invert the tree, meaning swap the left and right children of all nodes.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Args:
    root (list[Optional[int]]): Binary tree represented as a list (0-indexed, level order, None for missing nodes)

Returns:
    list[Optional[int]]: Inverted binary tree as a list (0-indexed, level order, None for missing nodes)
"""

def invert_binary_tree(root: list[int]) -> list[int]:
        q=[]
        if root is None:
            return None
        q.append(root)
        while len(q)!=0:
            node=q.pop(0)
            a=node.left
            node.left=node.right
            node.right=a
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
