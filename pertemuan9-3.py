#palindrom
#input
A1 = input("Masukkan Kata : ")

#proses
A2 = ''.join(reversed(A1))
if A1 == A2:
    print(A1, " adalah Palindrom")
else :
    print(A1, " bukan Palindrom")