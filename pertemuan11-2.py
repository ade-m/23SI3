def salam():
    print("Selamat Siang")

def inigenap_atau_ganjil(bilangan):
    if(bilangan%2==0):
        print(bilangan, " adalah bilangan genap")
    else :
        print(bilangan, " adalah bilangan ganjil")

def luasPersegi(sisi):
    return sisi*sisi

print(luasPersegi(10))
inigenap_atau_ganjil(8)
inigenap_atau_ganjil(101)
inigenap_atau_ganjil(7890)

for i in range(9):
    salam()

