#pengolahan string

kata1 = "Baju di Toko"
kata2 = """Layanan merujuk pada segala fasilitas 
atau manfaat yang disediakan oleh satu pihak kepada 
pihak lain dimana pada dasarnya hal tersebut bersifat 
abstrak dan tidak melibatkan kepemilikan terhadap 
suatu objek atau barang."""

print("Panjang kata 1=",len(kata1))
print("Panjang kata 2=",len(kata2))

for x in "Banana":
    print(x,end="+")
print()
print("baju" in kata1)
print("Jumlah Karakter A : ",kata2.count("pada"))

