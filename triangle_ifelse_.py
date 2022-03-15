a=int(input("Enter a first number"))
b=int(input("Enter a first number"))
c=int(input("Enter a first number"))

sum=a+b+c


if(sum==180):
    print("triangle is formed")

if((a==90) or (b==90) or (c==90)):
    print("it is right angle triangle")

if((a<90) and (b<90) and (c<90)):
    print("it is an acute angle triangle")

if((a>90) or (b>90) or (c>90)):
    print("it is an obtus angle triangle")

else:
    print("triangle is not formed")



