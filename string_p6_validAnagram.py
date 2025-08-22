# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        #Efficient Approach
def isAnagram( s, t):
        
        if len(s)!=len(t):
            return False
        maps={}
        mapt={}

        for i in s:
            maps[i]=maps.get(i,0)+1#by default zero agr exist nai krta
        for j in t:#frequency check krty hai words ki 
            mapt[j]=mapt.get(j,0)+1
        return maps==mapt




if __name__ =="__main__":
     s = "anagram"
     t = "nagaram"
     print(isAnagram(s,t))
     s = "rat"
     t = "car"
     print(isAnagram(s,t))
     #built maps
# a → maps.get('a',0)+1 = 0+1 = 1
# n → maps.get('n',0)+1 = 0+1 = 1  
# a → maps.get('a',0)+1 = 1+1 = 2
# g → maps.get('g',0)+1 = 0+1 = 1
# r → maps.get('r',0)+1 = 0+1 = 1
# a → maps.get('a',0)+1 = 2+1 = 3
# m → maps.get('m',0)+1 = 0+1 = 1

# maps = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
   #built mapt
# n → mapt.get('n',0)+1 = 0+1 = 1
# a → mapt.get('a',0)+1 = 0+1 = 1
# g → mapt.get('g',0)+1 = 0+1 = 1
# a → mapt.get('a',0)+1 = 1+1 = 2
# r → mapt.get('r',0)+1 = 0+1 = 1
# a → mapt.get('a',0)+1 = 2+1 = 3
# m → mapt.get('m',0)+1 = 0+1 = 1

# mapt = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

# Less Efficent Approach
# def isAnagram(s, t):
#         if len(s)!=len(t):
#             return False
#         return sorted(s)==sorted(t) 
