"""
Task 18: Decode String

Given an encoded string s, return its decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.

Example:
    decode_string(s="3[a2[c]]") -> "accaccacc"

Args:
    s (str): The encoded string (0-indexed)

Returns:
    str: The decoded string
"""

def decode_string(s: str) -> str:
    st=[]
    ans=""
    for i in range(len(s)):
        if s[i]!=']':
            st.append(s[i])
        else:
            ans=""
            while s[i]!='[':
                ans+=st.pop()
            st.pop()
            ans=ans*(st[len(st)-1]-'0')
            st.pop()
            st.append(ans)
    
    rev_ans=reversed(ans)
    return rev_ans


