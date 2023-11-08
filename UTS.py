#output
keranjang =["Roma Kelapa","Tawar Jumbo","Saos Kikkoman","Blue Band","Meises Ceres"]
keranjang2 =[1,2,3,1,2]
keranjang3 =[8000,18000,21900,10000,15000]

print("\n*****************************************************")
print("PT.IndoDesember  \nJl. Rame No.1")
print("*****************************************************")
print("\nNama Pelanggan \t \t Aldi Algoritma\n")
print("Nama Barang \t \t QTY  \t\t Harga")
print("=====================================================")
total =0
for i in range(5):
   print(keranjang[i]," \t\t ",keranjang2[i]," \t\t ",keranjang3[i])
   total += (keranjang2[i]*keranjang3[i])

print("\n\n\n=====================================================")
print("Total Belanjaan \t\t\t ",total)

keranjang =["Mito AF-1","Philips Mixer","Sharp Vacuum","Miyako Mixer","Modena M.Cuci"]
keranjang2 =[10,2,3,11,2]
keranjang3 =[978000,460000,849000,289000,7064000]

print("\n*****************************************************")
print("PT.Ujian Rabu  \nJl. Suka Jadi No.1")
print("*****************************************************")
print("\nNama Karyawan \t \t Vicky Algoritma")
print("Lokasi Gudang \t \t Pancing\n")
print("Nama Barang \t \t Stok  \t\t Harga")
print("=====================================================")
total =0
for i in range(5):
   print(keranjang[i]," \t\t ",keranjang2[i]," \t\t ",keranjang3[i])
   total += (keranjang2[i]*keranjang3[i])

print("=====================================================")
print("Total Asset \t\t\t\t ",total)