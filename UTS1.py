n= int(input("Masukkan N :"))
"""""
for i in range(1,n+1):
    print(i*3,end =",")
print("")
for i in range(1,n+1):
    print(i*i,end =",")
print("")
"""

print("a.", end=" ")
x=1
for i in range(1,n+1):
    print((2**i)*x,end =",")
    x *=-1

print("")

print("b.", end=" ")
x=2
for i in range(1,n+1):
    x=x*2
    print(x,end =",")

print("")
y=0
x=1
print("c.", end=" ")
print(y,end=",")
for i in range(1,n+1):
    print(x,end =",")
    tmpy=y
    y=x
    x=tmpy+x

print("")
print("d.", end=" ")
for i in range(1,n+1):
    x =1
    for j in range(1,i+1):
        x*=j
    print("2/",x,end =", ")


print("")
    