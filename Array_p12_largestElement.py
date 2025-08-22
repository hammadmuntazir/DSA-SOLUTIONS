# '''
# class solution hai usky class ky  method ko call krny ky liye
# object bnaye hain

# jub bi Python programming  mein hum object  oriented concept ko use krty hain
# to hum class ka aik object bnaty hain
# self  ki help sy ksi dusry variable method ko access krsky gyein
# '''
# from typing import List
# class Solution:
#     def largest(self,n:int ,arr:List[int])->int:
#         max=arr[0]
#         for i in range(1,n):
#             if arr[i]>max:
#                 max=arr[i]
#         return max

      #Finding Largest Element in Array
 #logic: subsy pahly block cko largest maan lo phir loop lga kr sary elements sy compare krlo agr koi bara hai to usay largest maan lo

def largest_elemet(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
# Driver code
if __name__ == "__main__":
    arr = [1, 4, 56, 89, 90]
    print("Largest element in the array is:", largest_elemet(arr))  # Output: 90
