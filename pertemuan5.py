#perulangan dengan for

#input
n=10
x=20
i=0

#perulangan 1 sampai n
for i in range(n):
    print(i+1, end='\t')
print("\n==========")
#perulangan 0 sampai n dengan incremental 2
for i in range(0,n-1,2):
    print(i+2, end=',')
print("\n==========")
#perulangan dari n sampai x+1 dengan incremental 1
for i in range(n,x+1,1):
    if((i%3)==0):
        print(i, end=' ')
print("\n==========")

