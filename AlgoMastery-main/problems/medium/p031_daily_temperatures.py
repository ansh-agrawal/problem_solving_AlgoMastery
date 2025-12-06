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

def daily_temperatures(temp: List[int]) -> List[int]:
    n=len(temp)
    temp_list=[]
    st=[]
    for i in range(n-1,-1,-1):
        if len(st)==0:
            temp_list.append(0)
        elif len(st)!=0 and st[-1][0]<=temp[i]:
            while len(st)!=0 and st[-1][0] <= temp[i]:
                st.pop()
            if len(st)==0:
                temp_list.append(0)
            else:
                temp_list.append(st[-1][1]-i)
        elif len(st)!=0 and st[-1][0] > temp[i]:
            temp_list.append(st[-1][1]-i)
        st.append((temp[i],i))
    temp_list.reverse()
    return temp_list
