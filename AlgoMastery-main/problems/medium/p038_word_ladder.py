"""
Task 38: Word Ladder

Given begin_word, end_word, and a list of word_list, return the length of the shortest transformation sequence from begin_word to end_word, such that only one letter can be changed at a time and each transformed word must exist in word_list. Return 0 if no such sequence exists. All words are 0-indexed.

Example:
    word_ladder(begin_word="hit", end_word="cog", word_list=["hot","dot","dog","lot","log","cog"]) -> 5
    word_ladder(begin_word="hit", end_word="cog", word_list=["hot","dot","dog","lot","log"]) -> 0

Args:
    begin_word (str): Starting word (0-indexed)
    end_word (str): Target word (0-indexed)
    word_list (list[str]): List of allowed words (0-indexed)

Returns:
    int: Length of shortest transformation sequence, or 0 if impossible
"""

def word_ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
        temp={}
        q=[]
        vis={}
        for i in range(len(wordList)):
            temp[wordList[i]]=i
        q.append([1,beginWord])
        while len(q)!=0:
            [num_steps,word]=q.pop(0)
            if word==endWord:
                return num_steps
            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):
                    temp_word=word[:i]+chr(j)+word[i+1:]
                    if temp_word in temp and temp_word not in vis:
                        vis[temp_word]=1
                        q.append([num_steps+1,temp_word])
            
        return 0