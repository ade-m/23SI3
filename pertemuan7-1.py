#program array sederhana

#input
#matakuliah Dasar Pemrograman, Konsep SI, Agama, Techskill, B. Indonesia, Leadership, PTI
namaMatakuliah =["Dasar Pemrograman", "Konsep SI", "Agama", "Techskill", "B. Indonesia", "Leadership", "PTI"]
nilaiMatakuliah = ["A","A-","A","B+","A","B+","C"]

#output
print(namaMatakuliah)
print(nilaiMatakuliah)
for x in namaMatakuliah:
    print(x)
for i in range(0,7):
    print("Nilai ",namaMatakuliah[i]," : ",nilaiMatakuliah[i])