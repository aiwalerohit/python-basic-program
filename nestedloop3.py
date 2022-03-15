n=int(input("enter a number"))
for r in range (1,n+1):
        for c in range (r, n+1):
            print('*', sep='\t', end='')
        print()