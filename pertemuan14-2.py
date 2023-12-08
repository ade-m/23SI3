def fibonancy(n):
    if n ==0 or n==1:
        return n
    else:
        return (fibonancy(n-1)+fibonancy(n-2))
    
x= int(input("Masukkan Batas Deret fibonancy : "))
print("Deret Fibonancy")
for i in range(x):
    print(fibonancy(i),end=" ")