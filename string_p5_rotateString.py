# Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
s = "abcde"
goal = "cdeab"
def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    return goal in (s+s)#goal in (s+s) already returns a boolean (True or False)


#driver code
if __name__ =="__main__":
    #example 1
    s = "abcde"
    goal = "cdeab"
    print(rotate_string(s,goal))
    #example 2
    s = "abcde" 
    goal = "abced"
    print(rotate_string(s,goal))