a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))

if((a+b)>c and (b+c)>a and (a+c)>b):
    print("It is triangle")

    if(a==b) and (b==c) and (a==c):
        print("Triangle is equilateral triangle")

    elif(a==b) or (b==c) or (c==a):
        print("Triangle is isosceles triangle")

else:
    print("Triangle is not found")