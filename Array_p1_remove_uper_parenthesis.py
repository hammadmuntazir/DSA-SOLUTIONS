#humy outermost parenthesis ko htana hai
#basically parsing krni hai
#(()())(())
#0123456789
#collection of character is string
#result mein andar waly parethsis ko jorna hai ["()()","()""]
#aik variable leta hu result=[] empty list
#aik variable ko pkar kr uska name balance rakh do balance=0
#humy idr index aur index pr rakhy hu element ko bi pkrana hai
# enumrate waly method sy string ky index aur character ko aik saat pakar kr chal skta hai for i,char in enumerate(s):
#subsy pahly balance ko check karin gye basicallly jub left wala bracket dekhy gye to value +1 krdain gye ,close wala bracket right wala dekh kr value -1 krdain gye
#balance ka value aik point pr akar zero ho jaye ga
# if char=='(': 
#    if bal==0:
#       start=i
#    bal+=1
# elif char==')'
#     bal-=1  # jub balance ka value zero hota to result mein append krdo s[start+1.:i]
#['()()']
#join method ko use kro



# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".

# def removeOuterParenthesis(s):
#     result=[]
#     balance=0
#     start=0

#     for i,char in enumerate(s):
#         if char == '(':
#             if balance==0:
#                 start=i
#             balance+=1
#         elif char ==')':
#             balance-=1
#             if balance==0:
#                 result.append(s[start+1:i])
#     return "".join(result)

# if __name__=="__main__":
#     s = "(()())(())"
#     print(removeOuterParenthesis(s))

#((()))(()())
#0123456789AB
def remove_uper_parenthesis(s):
    result=[]
    balance=0
    start=0

    for i,char in enumerate(s):
        if char=='(':
            if balance==0:
                start=i
            balance+=1
        elif char ==')':
            balance-=1
            if balance==0:
                result.append(s[start+1:i])
    return ''.join(result)

if __name__=="__main__":
    s = "(()())(())"
    print(remove_uper_parenthesis(s))
