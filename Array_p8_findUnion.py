# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

def findUnion(arr1,arr2):
   i,j=0,0
   union_set=[]
   last=None #track rakhy ga duplicate ka
   n=len(arr1)
   m=len(arr2)
   while i<n and j<m:
        if arr1[i] <arr2[j]: #array 1 ka element chota hai
            if last !=arr1[i]:
                union_set.append(arr1[i])
                last=arr1[i] 
            i+=1
            
        elif arr1[i]>arr2[j]:
            if last !=arr2[j]:
                union_set.append(arr2[j])
                last=arr2[j]
            j+=1

        else:   #dono equal ho gyein hain
            if last!=arr1[i]:
                union_set.append(arr1[i])
                last=arr1[i]
            i+=1
            j+=1
 
   while i<n:            
       if last!=arr1[i]:
           union_set.append(arr1[i])
           last=arr1[i]
       i+=1

   while j<m:
       if last!=arr2[j] :
           union_set.append(arr2[j])
           last=arr2[j]
       j+=1
   return union_set

#driver code
if __name__=="__main__":
    arr1=[1,2,3,8]
    arr2=[2,3,4,5,6]
    print(findUnion(arr1,arr2))

# 
