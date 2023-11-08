try:
    A = (input("A :"))
    B = (input("B :"))
    A=int(A)
    B=int(B)
    c = A/B
except ZeroDivisionError:
    print("A tidak boleh dibagi dengan 0")
    c="-"
except ValueError:
    print("A dan B harus di input menggunakan Angka")
    c="-"
except:
    print("Terjadi kesalahan pada program")
    c="-"

print("C : ",c)