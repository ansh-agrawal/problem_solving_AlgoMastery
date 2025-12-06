"""
Task 16: Longest Palindromic Substring

Given s, return the longest palindromic substring in s (0-indexed).

Example:
    longest_palindromic_substring(s="babad") -> "bab"  # or "aba"
    longest_palindromic_substring(s="cbbd") -> "bb"

Args:
    s (str): Input string (0-indexed)

Returns:
    str: Longest palindromic substring
"""
def longest_palin_length(left,right,s):
    while left>=0 and right<len(s)  and s[left]==s[right]:
        left-=1
        right+=1
    return left+1,right-1

def longest_palindromic_substring(s: str) -> str:
    max_len=0
    max_ind1=-1
    max_ind2=-1
    for i in range(len(s)):
        if len(s)%2==0:
            l1,l2=longest_palin_length(i,i+1,s)
        else:
            l1,l2=longest_palin_length(i,i,s)
        if l2-l1>max_len:
            max_len=l2-l1+1
            max_ind1=l1
            max_ind2=l2
    ans_str=s[max_ind1:max_ind2+1]
    return ans_str