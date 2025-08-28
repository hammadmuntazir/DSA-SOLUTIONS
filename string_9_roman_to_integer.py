# roman to integer
 
# link of question
# https://leetcode.com/problems/roman-to-integer/
def roman_to_integer(s):
    roman_to_int={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    previous=0

    for char in s:
        current=roman_to_int[char]
        if current>previous:
            total+=current-2*previous
        else:
            total+=current
        previous=current
    return total


if __name__ =="__main__":
    s = "III"
    print(roman_to_integer(s))
    s = "XLII"
    print(roman_to_integer(s))
    s = "DCCCXC"
    print(roman_to_integer(s))

# Logic
# Subtractive Notation: When a smaller numeral appears before a larger one, it's subtracted (IV = 4, IX = 9, etc.)

# Your Algorithm's Logic:

# If current numeral > previous numeral: total += current - 2 * previous

# This effectively subtracts the previous value twice (once for the addition, once for the subtraction)

# Time Complexity: O(n) where n is the length of the string

# Space Complexity: O(1) - only using a fixed dictionary and few variables