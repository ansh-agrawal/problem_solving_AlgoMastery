"""
Task 14: Longest Substring Without Repeating Characters

Given s, return the length of the longest substring without repeating characters (0-indexed).

Example:
    longest_substring_without_repeating_characters(s="abcabcbb") -> 3  # substring "abc"
    longest_substring_without_repeating_characters(s="bbbbb") -> 1

Args:
    s (str): Input string (0-indexed)

Returns:
    int: Length of longest substring without repeating characters
"""

def longest_substring_without_repeating_characters(nums: str) -> int:
    temp={}
    start=0
    end=0
    maxlen=0
    while end<len(nums):
        if nums[end] not in temp:
            temp[nums[end]]=1
            maxlen=max(maxlen,end-start+1)
            end+=1
        else:
            while start<end and nums[end] in temp:
                temp[nums[start]]-=1
                if temp[nums[start]]==0:
                    temp.pop(nums[start])
                start+=1
    return maxlen
