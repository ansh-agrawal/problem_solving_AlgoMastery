"""
Task 4: Container With Most Water

Given an array height, find two lines that together with the x-axis form a container, such that the container contains the most water.

Example:
    container_with_most_water(height=[1,8,6,2,5,4,8,3,7]) -> 49
    container_with_most_water(height=[1,1]) -> 1

Args:
    height (list[int]): Heights of lines (0-indexed)

Returns:
    int: Maximum area of water container
"""

def container_with_most_water(height: list[int]) -> int:
    area=1
    for i  in range(len(height)-1):
        for j in range(i+1,len(height)):
            min_val=min(height[i],height[j])
            area=max(area,min_val*(j-i))
    return area

