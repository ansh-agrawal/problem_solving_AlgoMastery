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

def word_ladder(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """
    Word Ladder.

    Args:
        begin_word (str): Starting word (0-indexed)
        end_word (str): Target word (0-indexed)
        word_list (list[str]): List of allowed words (0-indexed)

    Returns:
        int: Length of shortest transformation sequence, or 0 if impossible
    """
    # TODO: implement
    pass
