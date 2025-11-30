"""
Task 31: Daily Temperatures

Given a list of daily temperatures, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 for that day.

Example:
    daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0]
    daily_temperatures([30, 40, 50, 60]) -> [1, 1, 1, 0]
"""

from typing import Any, List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Compute the number of days to wait until a warmer temperature.

    Args:
        temperatures (List[int]): List of daily temperatures

    Returns:
        List[int]: List of days to wait for a warmer temperature
    """
    # TODO: implement
    pass
