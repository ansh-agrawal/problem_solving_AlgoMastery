"""
Task 66: Sum Root to Leaf Numbers

Given the root of a binary tree containing digits from 0-9 only, return the total sum of all root-to-leaf numbers. Each root-to-leaf path represents a number formed by concatenating the node values.

Example 1:
    Input: root = [1,2,3]
    Output: 25
    Explanation: The root-to-leaf numbers are 12 and 13, so sum is 12 + 13 = 25.

Example 2:
    Input: root = [4,9,0,5,1]
    Output: 1026

Args:
    root (list[Optional[int]]): Binary tree represented as a list (0-indexed, level order, None for missing nodes)

Returns:
    int: Total sum of all root-to-leaf numbers
"""
def list_of_numbers_root_leaf(root,lst,temp_str):
        if root is None:
            return None
        temp_str+=str(root.val)
        if root.left is None and root.right is None:
            lst.append(temp_str)
        list_of_numbers_root_leaf(root.left,lst,temp_str)
        list_of_numbers_root_leaf(root.right,lst,temp_str)

def sum_root_to_leaf_numbers(root: list[int]) -> int:
        lst=[]
        temp_str=""
        summ=0
        list_of_numbers_root_leaf(root,lst,temp_str)
        for i  in range(len(lst)):
            summ+=int(lst[i])
        return summ


