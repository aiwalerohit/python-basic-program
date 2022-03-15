#number divisible by 13 and 17

i=1

for i in range(1,101):
    if((i%13==0) or (i%17==0)):
        print(i)
