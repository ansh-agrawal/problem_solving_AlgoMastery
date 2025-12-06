"""
Task 30: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class with the following operations:
- push(val): Push element val onto the stack.
- pop(): Remove the element on top of the stack.
- top(): Get the top element.
- get_min(): Retrieve the minimum element in the stack.

Example:
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.get_min() -> -3
    stack.pop()
    stack.top() -> 0
    stack.get_min() -> -2
"""

from typing import Any

def min_stack(args: Any) -> Any:
    def __init__(self):
        self.st=[]
        self.min_val=2**31
        self.st1=[]

        

    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.min_val=val
            self.st1.append(val)
        self.st.append(val)
        

    def pop(self) -> None:
        if len(self.st1) > 0 and self.st[-1]==self.st1[-1]:
            self.st1.pop()
            if self.st1:
                self.min_val=self.st1[-1]
            else:
                self.min_val=2**31

        if len(self.st) > 0:
            self.st.pop()
            

    def top(self) -> int:
        if len(self.st) > 0:
            return self.st[-1]

        

    def getMin(self) -> int:
        if len(self.st1) > 0:
            return self.st1[-1]
