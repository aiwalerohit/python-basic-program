
km=int(input("Enter a km"))

if(km<=5):
    bill=3*km
    print("Bill amount is",bill)

elif((km>5) and (km<=10)):
        bill=5*km
        print("Bill amount is", bill)

elif((km>10) and (km<=15)):
        bill=7*km
        print("Bill amount is", bill)
elif((km>15) and (km<=20)):
        bill=9*km
        print("Bill amount is", bill)

else:
    bill=11*km
    print("Bill amount is", bill)