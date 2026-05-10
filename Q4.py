i =5
i+=1
print(i)

while i>=5:
    print(i)
    i-=1
# ------- ------------- ----------- 

i=1
while i<=100:
    print(i)
    i=i+1

#------------------- ------------

a=[1,4,9,16,25,36,49,64,100]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[8])

idx=0
while idx<= len(a):
    print(a[idx])
    idx= idx +1

# print the table of Number n
n=2
i=1
m=0
while i<=10:
    m=n*i
    print(m)
    i+=1 

print('hello')

n=121
original = n
s=0
while n>0:
    t = n%10
    s=s*10+t
    n=n//10

if  s==original :
  print("palindrome") 
   
else:  print('not ')
