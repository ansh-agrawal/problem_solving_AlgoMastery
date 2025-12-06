"""
Task 67: Convert Sorted Array to BST

Given an integer array nums where the elements are sorted in ascending order (0-indexed), convert it to a height-balanced binary search tree and return it as a list in level order.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,None,5]

Example 2:
    Input: nums = [1,3]
    Output: [3,1]

Args:
    nums (list[int]): Sorted array (0-indexed)

Returns:
    list[Optional[int]]: Height-balanced BST as a list (0-indexed, level order, None for missing nodes)
"""
# need to make TreeNode class
def sorted_array_to_bst(self,lst,start,end):
        if start>end:
            return None
        mid = start+(end-start)//2
        node=TreeNode(lst[mid])
        node.left=self.sorted_array_to_bst(lst,start,mid-1)
        node.right=self.sorted_array_to_bst(lst,mid+1,end)
        return node
def convert_sorted_array_to_bst(nums: list[int]) -> list[int]:
    return self.sorted_array_to_bst(nums,0,len(nums)-1)


