# 1903. Largest Odd Number in String

# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
# Example 2:

# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".
# Example 3:

# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.
 

# Constraints:

# 1 <= num.length <= 105
# num only consists of digits and does not contain any leading zeros.

#logic for  i in range(1,5) #output:1,2,3,4
#for i in range(5,1,-1)#output:5432
#for i in range(5,-1,-1)#output:543210
#  hum 52 ko dekhain gye is trah pahly 2 phir 5
#jidr odd number nazar aye ga udr brake laga lein gye
def largest_odd_num(num):
    for i in range(len(num)-1,-1,-1):
        if int[num[i]]%2 !=0:
            return num[:i+1]
    return ""

if __name__ =="__main__":
    num="52"
    print(largest_odd_num(num))