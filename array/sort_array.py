# sort array

# def sorted_array(arr):
#       arr.sort()
#       return arr

# arr=[3,4,1,2,9,5]
# print(sorted_array(arr))
def sort_array(arr):
    arr=arr[:]
    n=len(arr)
   
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaapped=True

        if not swapped:
            break
    return arr
