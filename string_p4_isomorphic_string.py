# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

   #Solution
#Two strings are isomorphic if:
#Each character in s maps to exactly one character in t

# Each character in t maps to exactly one character in s

# Example:
# Isomorphic:

# s = "egg", t = "add"

# e → a, g → d (consistent)

# a → e, d → g (consistent)

# Not Isomorphic:

# s = "foo", t = "bar"

# f → b, o → a, o → r (inconsistent: o maps to both a and r)
       #Key Rule
# 1)One-to-One Mapping: Each character in s must map to exactly one character in t, and vice versa.

# No Two-to-One Mapping:

# ❌ If two different characters in s map to the same character in t → Not isomorphic

# ❌ If one character in s maps to two different characters in t → Not isomorphic

# 2)Same Length: The strings must be of equal length.


def isomorphic(s,t):
    if len(s)!=len(t):# check if both length are different return False is not isomorphic
        return False
    #if both lengths are same
    st={}
    ts={}
    for i,j in zip(s,t):
        if i in st:
            if st[i]!=j:
                return False
        else:
            st[i]=j
        
        if j in ts:
            if ts[j]!=i:
                return False
        else:
            ts[j]=i
    return True


# driver code
if __name__ =="__main__":
    s = "egg"
    t = "add"
    print(isomorphic(s,t))