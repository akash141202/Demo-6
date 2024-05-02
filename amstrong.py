#Amstrong number

n=int(input("Enter a number:"))
a=n
count=0
while(n>0):
    n=n//10
    count=count+1
n=a
sum=0
while(n>0):
    b=n%10
    sum=sum+(b**count)
    n=n//10
if(sum==a):
    print("amstrong number")
else:
    print("not a amstrong number")
