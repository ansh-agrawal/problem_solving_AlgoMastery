"""
Task 94: Paint House

There is a row of n houses, each can be painted with one of k colors.
The cost of painting each house with a certain color is given by a cost matrix costs, where costs[i][j] is the cost of painting house i with color j.
You need to paint all the houses such that no two adjacent houses have the same color.
Return the minimum total cost to paint all houses.

Example:
    paint_house([[17,2,17],[16,16,5],[14,3,19]]) -> 10   # Paint house 0 with color 1, house 1 with color 2, house 2 with color 1
    paint_house([[1,5,3]]) -> 1                           # Only one house, choose min cost
"""

from typing import Any, List

def paint_house(costs: List[List[int]]) -> int:
    """
    Compute the minimum cost to paint all houses with no two adjacent houses having the same color.

    Args:
        costs (List[List[int]]): Cost matrix where costs[i][j] is the cost of painting house i with color j

    Returns:
        int: Minimum total painting cost
    """
    # TODO: implement
    pass
