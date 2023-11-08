#cek kapasitas meja
meja = ((1,6),(2,7),(3,3),(4,2),(5,2))
pelanggan = input("Daftar Nama Pelanggan : ")
listPelanggan = pelanggan.split(",")

for x in meja:
    if (x[1]>len(listPelanggan) and (len(listPelanggan)*2>x[1])):
        print("Pelanggan :",pelanggan)
        print("Meja Nomor", x[0])
        break

