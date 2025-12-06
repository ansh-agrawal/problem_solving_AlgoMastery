"""
Task 39: Binary Tree Maximum Path Sum

Given the root of a binary tree, return the maximum path sum. A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root. Tree nodes are 0-indexed.

Example:
    binary_tree_maximum_path_sum(root=[1,2,3]) -> 6
    binary_tree_maximum_path_sum(root=[-10,9,20,None,None,15,7]) -> 42

Args:
    root (list[Optional[int]]): Binary tree represented as a list (0-indexed, level order, None for missing nodes)

Returns:
    int: Maximum path sum
"""
class Treenode:

    def __init__(self,data_val):
        self.val=data_val
        self.left=None
        self.right=None


def buildTree(lst):
        if lst and lst[0]:
            root=Treenode(lst[0])
        q=[]
        q.append(root)
        i=1
        while q and i<len(lst):
            node=q.pop(0)
            if i<len(lst) and lst[i] is not None:
                node.left=Treenode(lst[i])
                q.append(node.left)
                i+=1
            if i<len(lst) and lst[i] is not None:
                node.right=Treenode(lst[i])
                q.append(node.right)
                i+=1
        return root
        
def binary_tree_maximum_path_sum(node_list: list[int]) -> int:

        root = buildTree(node_list)
        maxx=[-10**4]

        max_sum=maxSumPath(root,maxx)
        return maxx[0]

def maxSumPath(node,maxx):
        if node==None:
            return 0
        leftsum=max(0,maxSumPath(node.left,maxx))
        rightsum=max(0,maxSumPath(node.right,maxx))
        maxx[0]=max(maxx[0],node.val+leftsum+rightsum)
        return node.val+max(leftsum,rightsum)



