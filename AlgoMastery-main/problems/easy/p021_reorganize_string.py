"""
Task 21: Reorganize String

Given a string s, rearrange the characters so that no two adjacent characters are the same. If possible, return any valid rearrangement, otherwise return an empty string.

Example:
    reorganize_string(s="aab") -> "aba"
    reorganize_string(s="aaab") -> ""

Args:
    s (str): The input string (0-indexed)

Returns:
    str: A valid rearrangement or empty string if not possible
"""
import heapq

def reorganize_string(s: str) -> str:
    dict1={}
    for i in range(len(s)):
        dict1[s[i]]=dict1.get(s[i],0)+1
    
    max_heap=[(-cnt,char) for char,cnt in dict1]
    heapq.heapify(max_heap)
    ans=""
    while max_heap:
        cnt,char=heapq.heappop(max_heap)
        ans+=char
        cnt+=1
        if cnt<0:
            heapq.heappush(cnt,char)
    
    for i in range(len(ans)-1):
        if ans[i]==ans[i+1]:
            return ""
    return ans

