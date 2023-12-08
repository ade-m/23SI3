def faktorial(n):
    if n ==0 or n==1:
        return n
    else:
        return n*(faktorial(n-1))
    
x= int(input("Masukkan Batas Deret faktorial : "))
print("Deret Faktorial")
for i in range(1,x+1):
    print(f"{i}! = {faktorial(i)}", end=", ")