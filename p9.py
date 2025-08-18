# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missing_num(nums):
    n=len(nums)
    expecting_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return expecting_sum - actual_sum

#driver code
if __name__ == "__main__":
    nums = [0, 1, 3, 4]  # n = 4, missing 2
    print(missing_num(nums))  # Output: 2
    nums=[3,0,1]
    print(missing_num(nums))
    nums = [9,6,4,2,3,5,7,0,1]
    print(missing_num(nums))
 