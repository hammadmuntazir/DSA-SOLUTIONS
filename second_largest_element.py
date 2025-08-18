#for i in arr: //index ka use nai kr rahye ,array mein hi dore kr laga rahye

# Finding Second Largest Element in Array
#logic:subsy pahly 2 block ly lo largest aur second largest dono mein -1 value store krva lo
#array ky elemnt pr loop chalyo agr koi value largest se bari hai to largest ki pahly vali value ko second largest mein store krva do aur largest ki value ko update krdo new value se
# agr koi value second largest se bari hai mgr largest nai hai phir second largest ki value ko update krdo

def second_largest_element(arr):
    largest_element=second_largest_element=-1
    for num in arr:
        if num>largest_element:
            second_largest_element = largest_element
            largest_element = num

        elif num>second_largest_element and num!=largest_element:
            second_largest_element=num
    return second_largest_element

# Driver code
if __name__ == "__main__":
    arr = [1, 4, 56, 89, 90]
    print("Second largest element in the array is:", second_largest_element(arr))  # Output: 89