from collections import Counter
"""
Task 17: Minimum Window Substring

Given two strings s and t, return the minimum window substring of s that contains all the characters of t (including duplicates). If there is no such substring, return an empty string.

Example:
    minimum_window_substring(s="ADOBECODEBANC", t="ABC") -> "BANC"

Args:
    s (str): The source string (0-indexed)
    t (str): The target string (0-indexed)

Returns:
    str: The minimum window substring containing all characters of t
"""
def has_all_needed(have: dict, need: dict) -> bool:
        for ch, cnt in need.items():
            if have.get(ch, 0) < cnt:
                return False
        return True
def minimum_window_substring(s: str, t: str) -> str:
    # start=end=0
    # temp1={}
    # for i  in range(len(t)):
    #     temp1[t[i]]=temp1.get(t[i],0)+1
    # temp2={}
    # ans_str=""
    # min_val=len(s)+1
    # while end<len(s):
    #     if temp2.items()<=temp1.items():
    #         temp2[s[end]]=temp2.get(s[end],0)+1
    #         min_val=min(min_val,end-start+1)
    #         ans_str=s[start:end+1]
    #         end+=1
    #     elif temp2>=temp1:
    #         while start<end and temp2.items()>=temp1.items():
    #             min_val=min(min_val,end-start+1)
    #             ans_str=s[start:end+1]
    #             temp2[s[start]]=temp2.get(s[start],0)-1
    #             if temp2[s[start]]==0:
    #                 temp2.pop(s[start])
    #             start+=1
    #         end+=1
    # return ans_str
    
    # Helper function: checks if 'have' contains required counts from 'need'

    start = end = 0
    temp1 = {}  # required counts
    for ch in t:
        temp1[ch] = temp1.get(ch, 0) + 1

    temp2 = {}  # current window counts
    ans_str = ""
    min_val = len(s) + 1

    while end < len(s):
        # Expand window to the right
        temp2[s[end]] = temp2.get(s[end], 0) + 1
        end += 1

        # When we have all needed chars, try shrinking from the left
        while has_all_needed(temp2, temp1):
            if end - start < min_val:
                min_val = end - start
                ans_str = s[start:end]

            temp2[s[start]] -= 1
            if temp2[s[start]] == 0:
                temp2.pop(s[start])
            start += 1

    return ans_str
        
