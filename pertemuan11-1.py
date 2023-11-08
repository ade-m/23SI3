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
nilais = input("Input (1-999):")
nilai=""
#ratusan

#ratusan
if(len(nilais)==1):
    nilai= " "
elif(len(nilais)==2):
    nilai= " "
else :
    nilai= nilais[0]

bacaAngka(nilai)
print(" Ratus", end=" ")

#ratusan
if(len(nilais)==1):
    nilai= " "
elif(len(nilais)==2):
    nilai= nilais[0]
else :
    nilai= nilais[1]
bacaAngka(nilai)
print(" Puluh", end=" ")


#satuan
if(len(nilais)==1):
    nilai= nilais[0]
elif(len(nilais)==2):
    nilai= nilais[1]
else :
    nilai= nilais[2]

bacaAngka(nilai)


print(" ")