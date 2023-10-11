#program array sederhana, 
#user menginput nilai dan nama matakuliah

#input
#matakuliah Dasar Pemrograman, Konsep SI, Agama, Techskill, B. Indonesia, Leadership, PTI

n = int(input("Jumlah Matakuliah : "))
namaMatakuliah =[" " for i in range(n)]
nilaiMatakuliah = [" " for i in range(n)]
for i in range(n):
    tmpnamaMatakuliah = input("Nama Mata Kuliah : ")
    tmpnilaiMatakuliah = input("Nilai Mata Kuliah : ")
    namaMatakuliah[i] = tmpnamaMatakuliah
    nilaiMatakuliah[i] = tmpnilaiMatakuliah

#output
print(namaMatakuliah)
print(nilaiMatakuliah)
print("Nama Matakuliah \t\t Nilai")
print("========================================")
for i in range(n):
   print(namaMatakuliah[i]," \t\t ",nilaiMatakuliah[i])