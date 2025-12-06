"""
Task 11: Spiral Matrix

Given a matrix, return all elements of the matrix in spiral order (0-indexed).

Example:
    spiral_matrix(matrix=[[1,2,3],[4,5,6],[7,8,9]]) -> [1,2,3,6,9,8,7,4,5]

Args:
    matrix (list[list[int]]): 2D matrix (0-indexed)

Returns:
    list[int]: Elements in spiral order
"""

def spiral_matrix(nums: list[list[int]]) -> list[int]:
    left,top = 0,0
    right,bottom =len(nums[0])-1, len(nums)-1
    temp=[]
    while left<=right and top<=bottom:
        for i  in range(left,right+1):
            temp.append(nums[top][i])
        top+=1
        for i in range(top,bottom+1):
            temp.append(nums[i][right])
        right-=1
        for i in range(right,left-1,-1):
            temp.append(nums[bottom][i])
        bottom-=1
        for i in range(bottom,top-1,-1):
            temp.append(nums[i][left])
        left+=1
    return temp