# Given an array of integers nums and an integer target, 
# find the smallest index (0 based indexing) where the target
# appears in the array. If the target is not found in the array,
# return -1
          
#->Linear search bari bari elements ko check kry ga target element ko dhondy ky lie
# complexity hogi O(n)

#binary search divide and conquer rule use kry ga  ,half array mein search kry ga
#complexity hogi 0(logn)

#         # By linear search

# def linear_search(nums,target):
#     for i in range(len(nums)):
#         if nums[i]==target:
#             return i
#     return -1

# #driver code
# if __name__ =="__main__":
#     nums=[1,2,3,4,5]
#     target=4
#     print (linear_search(nums,target))

#     nums=[5,6,6,7,9]
#     target=6
#     print(linear_search(nums,target))

          #Binary search
#logic is mein 3 cases hogyein   #k is mid
#hum 2 name ly gye aik p aur aik q start aur end pr
#1)target element middle mein ho p aur q ky #p+q//2
       #arr[mid]==target:
# 2)target element middle sy chotta ho is case mein q middle sy aik number pahly ajayae ga
# target<arr[mid] and q will become q=k-1

#3) target element middle sy bara ho is mein p middle sy aik number baad ho jaye ga
# target>arr[mid] and p wil become p=k+1

# yeah 3no kaam while loop mein us time tak krny hai jub tak p and q aik dusry ko cross nai krjaty ya equal nai ho jaty


def searchInSort(nums,k):
    p,q=0,len(nums)-1
    
    while p<=q:
         mid =p+(q-p)//2 #to prevent overflow direct mid=left+right//2 bi likh skty
         if nums[mid]==k:
              return mid
         elif nums[mid]<k:
              p=mid+1
         else:
              q=mid-1
    return -1

#driver code

if __name__=="__main__":
     nums=[1,2,3,4,5,6]
     k=5
print(searchInSort(nums,k))

