#Given an integer array nums,
#rotate the array to the right by k steps,
# where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

          #Logic
#->Reverse complete Array
#->Reverse first k elements
#->Reverse remaining elements(n-k elements)

def rotate(nums,k):
    n=len(nums)
    k=k%n  # To handle cases where k is greater than n

    def reverse(start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    
    reverse(0,n-1)  # Reverse the entire array
    reverse(0,k-1)  # Reverse the first k elements
    reverse(k,n-1)  # Reverse the remaining elements
        # Driver code

if __name__ == "__main__":
    # Test case 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print("Rotated array:", nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    rotate(nums2, k2)
    print("Rotated array:", nums2)  # Output: [3, 99, -1, -100]
