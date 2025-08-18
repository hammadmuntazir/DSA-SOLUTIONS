# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
# nums=[1,0,1,1,0,1]
def max_consective_one(nums):
    current_count=0
    max_count=0

    for num in nums:
        if num==1:
            current_count+=1
            max_count=max(max_count,current_count)
        else:
            current_count=0
    return max_count


#driver code
if __name__=="__main__":
    nums = [1,0,1,1,0,1]
    print(max_consective_one(nums))
    nums = [1,1,0,1,1,1]
    print(max_consective_one(nums))