def bacaAngka(nilai):
    if(nilai=="1"):
        print("Satu",end=" ")
    elif(nilai=="2"):
        print("Dua",end=" ")
    elif(nilai=="3"):
        print("Tiga",end=" ")
    elif(nilai=="4"):
        print("Empat",end=" ")
    elif(nilai=="5"):
        print("Lima",end=" ")
    elif(nilai=="6"):
        print("Enam",end=" ")
    elif(nilai=="7"):
        print("Tujuh",end=" ")
    elif(nilai=="8"):
        print("Delapan",end=" ")
    elif(nilai=="9"):
        print("Sembilan",end=" ")
    elif(nilai=="0"):
        print("Nol",end=" ")
    else:
        print(" ")
    
#input dan inisialisasi
matakuliah = [["MK001","DASAR PEMROGRAMAN",3],
          ["MK002","TECHSKILL",2],
          ["MK003","BAHASA INDONESIA",2],
          ["MK004","BAHASA INGGRIS",3],
          ["MK005","KEWARGANEGARAAN",2],]

nama=""
banyakMK=0
totalSKS=0
totalNILAI=0


nama = input("Nama Mahasiswa : ")
#input membership dan banyak belanjaan
banyakMK= int(input("Banyak Matakuliah : "))
tmpmatakuliah= [0 for i in range(banyakMK)]
tmpnilai= [0.0 for i in range(banyakMK)]
#perulangan untuk menginput produk ke keranjang
for x in range(banyakMK):
    #cetak membership yang tersedia
    for i in range(len(matakuliah)):
        print(i+1, ". ", matakuliah[i][0],
            " \t ", matakuliah[i][1],
            " \t ", matakuliah[i][2])
    kodeMK = input("Kode Matakuliah :")
    noMK =0
    
    for i in range(len(matakuliah)):
        if(matakuliah[i][0]==kodeMK):
            noMK = i
            print(i+1, " ", matakuliah[i][0],
            " \t ", matakuliah[i][1],
            " \t ", matakuliah[i][2])

    tmpmatakuliah[x] = noMK
    totalSKS += matakuliah[tmpmatakuliah[x]][2]
    totalNILAI += float(input("Masukkan Bobot Nilai :"))


#output
print("Nama Mahasiswa : ",nama)
print("Total SKS \t: ",totalSKS)
print("Total Bobot Nilai \t: ",totalNILAI/banyakMK)
strNilai = str(round(totalNILAI/banyakMK,1))
nilaiSplit = strNilai.split(".")
print(" Bobot Nilai Terbilang : ",end="")
bacaAngka(nilaiSplit[0])
print(" Koma ",end="")
bacaAngka(nilaiSplit[1][0])

print("\nDaftar Matakuliah")
for i in range(banyakMK):
    print(i+1, ". ", matakuliah[tmpmatakuliah[i]][0],
            " \t", matakuliah[tmpmatakuliah[i]][1],
            " \t", matakuliah[tmpmatakuliah[i]][2])
print("================================")








