# PRIME NUMBER 

# n = int(input("enter number : "))
# prime = True

# for i in range(2, n):
#     if n % i == 0:
#         prime = False
#         break

# if prime:
#     print("Prime")
# else:
#     print("Not Prime")
    
#FIBONACHI SERIES 
    
# a = int(input("enter number : "))
# b = int(input("enter number : "))

# for i in range(10):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c    
    
# PALINDROME NUMBER (READ FORWARD = READ BACKWORD)

# n = int(input("Enter :"))

# temp = n
# rev = 0

# while n > 0 :
#     digit = n % 10
#     rev = rev*10 + digit 
#     n =n//10
    
# if temp == rev :
#     print("PALINDROME") 
         
# else:
#     print("NOT PALINDROME") 
      
        
# n = 121

# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#  REVERSE OF STRING 

# str1 = "hello"
# temp = str1
# rev = ""

# for i in range(len(str1)-1, -1, -1):
#     rev = rev + str1[i]

# print(rev)
    
# if temp == rev:
#     print("palindrome")
    
# else:
#     print("not")

# FREQUENCY OF ELEMENT 

arr = [1, 2, 2, 3, 1]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)