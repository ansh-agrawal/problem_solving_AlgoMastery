"""
Task 29: Valid Parentheses

Given a string s containing only '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.

Examples (0-indexed):
    valid_parentheses("()[]{}") -> True
    valid_parentheses("(]") -> False
    valid_parentheses("([{}])") -> True
"""

def valid_parentheses(s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if len(st)==0 or (s[i]!='}' and s[i]!=']' and  s[i]!=')'):
                st.append(s[i])
            elif len(st)!=0 and ((s[i]=='}' and st[-1]!='{') or (s[i]==']' and st[-1]!='[') or (s[i]==')' and st[-1]!='(')):
                return False
            else:
                st.pop()
                
        if len(st)==0:
            return True
        return False
