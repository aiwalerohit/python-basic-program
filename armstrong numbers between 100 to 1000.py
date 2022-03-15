for i in range(100,1001):
    n=i
    sum=0

    while(n>0):
        d=n%10
        cube=d*d*d
        sum=sum+cube
        n=n//10

    if(i==sum):
        print(i)