"""
Task 3: Merge Intervals

Given a list of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return a list of the merged intervals (0-indexed).

Example:
    merge_intervals(intervals=[[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]
    merge_intervals(intervals=[[1,4],[4,5]]) -> [[1,5]]

Args:
    intervals (list[list[int]]): List of intervals (0-indexed)

Returns:
    list[list[int]]: Merged intervals
"""

def merge_intervals(nums: list[list[int]]) -> list[list[int]]:
    temp = []
    for i in range(len(nums)):
       if len(temp)==0:
           temp.append(nums[i])
       elif len(temp)!=0 and (nums[i][0]<=temp[len(temp)-1][1] and nums[i][1]<temp[len(temp)-1][1]):
           pass
       elif len(temp)!=0 and nums[i][0]<=temp[len(temp)-1][1]:
           temp[len(temp)-1][1] = nums[i][1]
       else:
           temp.append(nums[i])
    return temp