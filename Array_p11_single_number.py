# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

# is mein hum XOR operator bi use karty hain jisy 
# python mein assy show krty hain ^
#XOR ka truth table
#0^0=0
#1^1=0
#1^0=1
#0^1=1


#logic 
#let's suppose [0,0,1] hai 
#result=0
# 0^0=0
#0(result wala)^0=0
#0(result wala)^1=1
#yahi one single number hoga 

#ab aik aur case lety hain [2,2,1]
#result=0
#0^2=   binary mein kro aur dekho 000 ^010 =10=2
#2^2=0   same number ka xor zero hi hoga 010^010=0
#0^1=1  yahi1 single number hai

def single_number(nums):
    result=0
    for num in nums:
        result^=num

    return result
