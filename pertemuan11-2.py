def salam():
    print("Selamat Siang")

def inigenap_atau_ganjil(bilangan):
    if(bilangan%2==0):
        print(bilangan, " adalah bilangan genap")
    else :
        print(bilangan, " adalah bilangan ganjil")

def luasPersegi(sisi):
    luas = sisi*sisi
    return luas

luas = luasPersegi(10)
print(luas)
inigenap_atau_ganjil(8)
inigenap_atau_ganjil(101)
inigenap_atau_ganjil(7890)

for i in range(9):
    salam()

