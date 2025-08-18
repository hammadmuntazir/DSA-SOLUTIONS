# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 
#logic:
#-->aik hi bari mein krna hai two elements ly gyein i.e two pointer approach
def move_zeros(nums):
    n=len(nums)
    j=0
    for i in range(n):
        if nums[i]!=0:
            nums[j],nums[i]=nums[i],nums[j]
            j+=1

# Driver code
if __name__ == "__main__":
    # Test case 1
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    print("Array after moving zeros:", nums)  # Output: [1, 3, 12, 0, 0]

    # Test case 2
    nums2 = [0, 0, 1]
    move_zeros(nums2)
    print("Array after moving zeros:", nums2)  # Output: [1, 0, 0]