# # 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


def longest_common_prefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    First=strs[0]
    Last=strs[-1]
    ans=""
    for i in range(min(len(First),len(Last))):
        if First[i]!=Last[i]:
            return ans
        ans+=First[i]
    return ans


#driver code
if __name__ =="__main__":
    strs = ["flower","flow","flight"]
    print(longest_common_prefix(strs))

