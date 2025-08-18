#  Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
                  #Urdu
# Humain ek array diya gaya hai (nums). Humain check karna hai ke kya ye array pehlay non-decreasing order mein sorted tha aur phir rotate hua tha (0 ya zyada positions). Agar haan tou True return karo, warna False.
     
                    #Key Points:
 #-># Non-decreasing Order: Each element is ≤ the next one (e.g., [1, 2, 2, 3]). Non-decreasing Order: Har next element barha ya equal ho (masalan [1, 2, 2, 3])


#-># Rotation: Shifting elements circularly (e.g., rotating [1, 2, 3] by 1 gives [3, 1, 2]).Rotation: Elements ko circular shift karna (masalan [1, 2, 3] ko 1 position rotate karne se [3, 1, 2] ban jata hai)


# Duplicates Allowed: The array may contain duplicates (e.g., [2, 2, 2]).



#     Logic:

def check(nums):
    n = len(nums)
    if n <= 1:  # Edge case: empty or single-element array is always sorted
        return True
    count = 0
    for i in range(n):
        # Circular comparison: wraps around to compare last element with first
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    # At most one dip allowed for rotated sorted array
    return count <= 1# Driver code
if __name__ == "__main__":
    nums = [2, 2, 2, 3, 1]
    print(check(nums))  # Output: True
    nums = [1, 2, 3, 4, 5]
    print(check(nums))  # Output: True
    nums = [2, 1, 3, 4]
    print(check(nums))  # Output: False
    
#nums[i]>nums[i+1%n] ye logic sirf aik hi baar true hoga sortede and rotated array mein, agar ye condition do baar true ho rahi hai to iska matlab ye array sorted and rotated nahi hai.matlb count 0 sy 1 ho jaye ga
#nums[i]<nums[i+1%n] ye condition sirf aik hi baar true nai hogi

# Ek se zyada dips (nums[i] > nums[i+1]) → False

# Ek dip → last <= first check karo

# Zero dips → already sorted (True)