#input dan inisialisasi
produk = [["Piatos",10000],
          ["Kacang Kulit",20000],
          ["Coklat",20000],
          ["Oreo",10000]]
membership = [["Silver",5],
              ["Gold",10],
              ["Platinum",15]]
namaPelanggan=""
membershipPelanggan=0
banyakBelanja=0
totalBelanjaan=0
totalDiskon=0


namaPelanggan = input("Nama Pelanggan : ")
print("Pilih Membership :")
#cetak membership yang tersedia
for i in range(len(membership)):
    print(i+1, ". ", membership[i][0],
          " ", membership[i][1],"%")
#input membership dan banyak belanjaan
membershipPelanggan= int(input("Pilihan Membership (1/2/3) : "))-1
banyakBelanja= int(input("Banyak Belanjaan : "))
keranjangBelanja= [0 for i in range(banyakBelanja)]

#perulangan untuk menginput produk ke keranjang
for x in range(banyakBelanja):
    #cetak membership yang tersedia
    for i in range(len(produk)):
        print(i+1, ". ", produk[i][0],
            " IDR.", produk[i][1])
keranjangBelanja[x] = int(input("Pilihan Produk(1/2/3/4) :"))-1
    totalBelanjaan += produk[keranjangBelanja[x]][1]

totalDiskon = (totalBelanjaan*(membership[membershipPelanggan][1]/100))
totalBayar = totalBelanjaan-totalDiskon

#output
print("Daftar Belanjaan")
for i in range(banyakBelanja):
    print(i+1, ". ", produk[keranjangBelanja[i]][0],
            " IDR.", produk[keranjangBelanja[i]][1])
print("================================")
print("Total Belanja :",totalBelanjaan)
print("Total Diskon  :",totalDiskon)
print("Total Bayar   :",totalBayar)







