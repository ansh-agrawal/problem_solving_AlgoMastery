"""
Task 40: House Robber

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police (cannot rob adjacent houses). Houses are 0-indexed.

Example:
    house_robber(nums=[1,2,3,1]) -> 4
    house_robber(nums=[2,7,9,3,1]) -> 12

Args:
    nums (list[int]): Amount of money at each house (0-indexed)

Returns:
    int: Maximum amount of money that can be robbed
"""

def house_robber(nums: list[int]) -> int:

        dp=[0 for _ in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            if i-2>=0:
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            else:
                dp[i]=max(dp[i-1],nums[i])
        return dp[len(dp)-1]
        

