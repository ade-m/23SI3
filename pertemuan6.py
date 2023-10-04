z=5
z = int(input('input nilai :'))
for i in range(z):
    for j in range(i):
        print(j+1, end='')
    print('\n')
for i in range(z,0,-1):
    for j in range(i):
        print(j+1, end='')
    print('\n')


