# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

    #terms of question
#->in-place mean koi additional memory ka use nai krna usi array ko modify krna hai


def  removeDuplicates(nums):
    if not nums:
        return 0
    k = 1  # Initialize the count of unique elements
    for i in range(1,len(nums)):
        if(nums[i]!=nums[i-1]):
            nums[k]=nums[i]
            k+=1
    return k

#Driver code
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 5]
    k = removeDuplicates(nums)
    print("Number of unique elements:", k)  # Output: 5
    print("Modified array:", nums[:k])  # Output: [1, 2, 3, 4, 5]   