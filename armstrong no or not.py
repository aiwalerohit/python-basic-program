n=int(input("Enter a number"))

temp=n
sum=0

while(n>0):
    d=n%10
    cube=d*d*d
    sum=sum+cube
    n=n//10

print("sum of cube of digits=",sum)

if(temp==sum):
    print("armstrong number")

else:
    print("Its not armstrong number")