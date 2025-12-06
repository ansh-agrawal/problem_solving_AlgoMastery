"""
Task 8: Longest Consecutive Sequence

Given nums, return the length of the longest consecutive elements sequence (0-indexed).

Example:
    longest_consecutive_sequence(nums=[100, 4, 200, 1, 3, 2]) -> 4  # The sequence is [1,2,3,4]

Args:
    nums (list[int]): List of integers (0-indexed)

Returns:
    int: Length of the longest consecutive sequence
"""

def longest_consecutive_sequence(nums: list[int]) -> int:
    dp = [1]*len(nums)
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==1:
            dp[i]=dp[i]+dp[i-1]
    maxx=0
    for i in range(len(dp)):
        if dp[i]>maxx:
            maxx=dp[i]

    return maxx
