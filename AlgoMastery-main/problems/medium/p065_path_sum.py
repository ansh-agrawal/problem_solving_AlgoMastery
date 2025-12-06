"""
Task 65: Path Sum

Given the root of a binary tree and an integer target_sum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum.

Example 1:
    Input: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], target_sum = 22
    Output: True

Example 2:
    Input: root = [1,2,3], target_sum = 5
    Output: False

Args:
    root (list[Optional[int]]): Binary tree represented as a list (0-indexed, level order, None for missing nodes)
    target_sum (int): Target sum value

Returns:
    bool: True if such a path exists, False otherwise
"""
def targetPathSum(root,target,summ):
        if root is None:
            return False
        summ+=root.val
        if root.left is None and root.right is None:
            if summ==target:
                return True
            else:
                return False
        return targetPathSum(root.left,target,summ) or targetPathSum(root.right,target,summ)

def path_sum(root: list[int], target_sum: int) -> bool:
        summ=0
        return targetPathSum(root,target_sum,summ)

