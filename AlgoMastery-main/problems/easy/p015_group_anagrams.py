"""
Task 15: Group Anagrams

Given strs, group the anagrams together (0-indexed).

Example:
    group_anagrams(strs=["eat","tea","tan","ate","nat","bat"]) -> [["eat","tea","ate"],["tan","nat"],["bat"]]

Args:
    strs (list[str]): List of strings (0-indexed)

Returns:
    list[list[str]]: Grouped anagrams
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    dict1={}
    for i in range(len(strs)):
        word="".join(sorted(strs[i]))
        if word not in dict1:
            dict1[word]=[]
        dict1[word].append(strs[i])
    return list(dict1.values())

