#program untuk test fungsi array
#input
A = [23,5,79,100,30,7,2]
#B = (23,5,79,100,30,7,2)
print("A : ", A)
A.remove(100)
print("A : ", A)
A.pop()
print("A : ", A)
A.pop()
print("A : ", A)
print("Kemunculan 79 di A : ", A.count(79))
A.append(79)
print("A : ", A)
print("Kemunculan 79 di A : ", A.count(79))
print("Banyak Data A : ", len(A))
A.sort()
print("A : ", A)
A.reverse()
print("A : ", A)
Prima = [1,2,3,5,7]
A.extend(Prima)
print("A : ", A)

B = (23,5,79,100,30,7,2)
B[1]= 80
