n=125
original = n
s=0
while n>0:
    t = n%10
    s=s*10+t
    n=n//10

if  s==original :
  print("palindrome") 
   
else:  print('not ')

print('hello')