"""
Task 34: Sliding Window Maximum

Given an integer array nums and a sliding window size k,
return an array of the maximum values in each sliding window of size k moving from left to right.

Example:
    sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
    sliding_window_maximum([1], 1) -> [1]
    sliding_window_maximum([1,-1], 1) -> [1,-1]
"""

from typing import Any, List
from collections import deque
def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
        dq=deque()
        temp_lst=[]
        for i in range(k):
            if len(dq)!=0 and nums[i] > dq[-1][0]:
                while len(dq)!=0 and nums[i] > dq[-1][0]:
                    dq.pop()
            dq.append((nums[i],i))
        temp_lst.append(dq[0][0])
        for i in range(k,len(nums)):
            if dq[0][1]==i-k:
                dq.popleft()
            if len(dq)!=0 and nums[i] > dq[-1][0]:
                while len(dq)!=0 and nums[i] > dq[-1][0]:
                    dq.pop()
            dq.append((nums[i],i))
            temp_lst.append(dq[0][0])
        return temp_lst
