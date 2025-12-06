"""
Task 19: Valid Anagram

Given two strings s and t, return True if t is an anagram of s, and False otherwise.

Example:
    valid_anagram(s="anagram", t="nagaram") -> True
    valid_anagram(s="rat", t="car") -> False

Args:
    s (str): First string (0-indexed)
    t (str): Second string (0-indexed)

Returns:
    bool: True if t is an anagram of s, False otherwise
"""

def valid_anagram(s: str, t: str) -> bool:
    dict1={}
    dict2={}
    for i in range(len(s)):
        dict1[s[i]]=dict1.get(s[i],0)+1
    for i in range(len(t)):
        dict2[t[i]]=dict2.get(t[i],0)+1
    return dict1==dict2



