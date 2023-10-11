#program array sederhana, 
#user menginput nilai dan nama matakuliah

#input
#matakuliah Dasar Pemrograman, Konsep SI, Agama, Techskill, B. Indonesia, Leadership, PTI

n = int(input("Jumlah Matakuliah : "))
namaMatakuliah =[" " for i in range(n)]
nilaiMatakuliah = [0 for i in range(n)]
nilaiHurufMatakuliah = [" " for i in range(n)]
for i in range(n):
    tmpnamaMatakuliah = input("Nama Mata Kuliah : ")
    tmpnilaiMatakuliah = int(input("Nilai Mata Kuliah (0-100): "))
    namaMatakuliah[i] = tmpnamaMatakuliah
    nilaiMatakuliah[i] = tmpnilaiMatakuliah
    tmpnilaiHuruf=""
    if (tmpnilaiMatakuliah>=90):
        tmpnilaiHuruf="A"
    elif ((80>= tmpnilaiMatakuliah) and (tmpnilaiMatakuliah<90)):
        tmpnilaiHuruf="B"
    else:
        tmpnilaiHuruf="C"
    nilaiHurufMatakuliah[i] = tmpnilaiHuruf


#output

print("Nama Matakuliah \t Nilai \t Nilai Huruf")
print("=====================================================")
for i in range(n):
   print(namaMatakuliah[i]," \t\t ",nilaiMatakuliah[i]," \t ",nilaiHurufMatakuliah[i])