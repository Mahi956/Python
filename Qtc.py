# Type casting :-
# 1. implicit typecasting 
# 2. ecplicit typecasting 

# a = "1"
# b = "7"
# print (a+b) # but a & b are string 

# print (int(a) + int (b))  # now a & b will convert in int then they add 

# #--------IMPLICIT ------
# X = 1.22
# Y = 5
# print( X + Y)

arr = [1, 2, 3,4,3, 2, 4, 1]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):

        if arr[i] == arr[j]:
            print(arr[i])