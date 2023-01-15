import numpy as np
import pandas

#KONSTANTA
V = 15
R = 4.7
L = 50*(10**(-3))
C = 10**(-3)
x = 0
y = V/R
z = 0
h = 0.002
dt = 0.1

print("========================================")
print("Pilih metode perhitungan yang diinginkan")

bo = True
while bo == True:
    rules = input('\n1. Metode Euler \n2. Metode Heun \n3. Metode Runge Kutta Orde 4 \n\nPilihan: ')
    
    if rules == "1" or rules == "2" or rules == "3":
        bo = False
    
    else:
        print("Silahkan masukkan angka 1, 2, atau 3 saja")
        bo = True
        
if rules == "1":
    partisi = int(dt/h)     #int biar positif
    A = [[0 for x in range(partisi + 1)] for y in range (3)]

    #Mengenai Nilai awal
    A[0][0] = x
    A[1][0] = y
    A[2][0] = x*y/C

    for i in range(partisi):
        #Slope nya
        s = z 
        j = (-R*z-y/C)/L
        
        #Untuk iterasi selanjutnya
        yn = y + h*s
        zn = z + h*j
        
        #Mempersiapkan iterasi selanjurnya+store hasil
        y = yn
        z = zn
        x += h

        A[0][i+1] = x
        A[1][i+1] = yn
        
        #Mencari nilai v untuk iterasi i+1 atau untuk t=(i+1)*0,002
        A[2][i+1] = A[0][i+1] * A[1][i+1] / C

    df = {'t' : A[0], 'I' : A[1], 'V_c' : A[2]}
    
    print("==============================")
    print("Hasil perhitungan Metode Euler\n")
    print(pandas.DataFrame(data = df))

if rules == "2":
    partisi = int(dt/h)    #int biar positif
    A = [[0 for x in range(partisi + 1)] for y in range (3)]
    
    #Mengenai Nilai awal
    A[0][0] = x
    A[1][0] = y
    A[2][0] = x*y/C
    
    for i in range(0,partisi):
        #Slope
        s = z #s=slope 
        j = (-R*z-y/C)/L
        
        #Untuk iterasi selanjutnya
        #Prediktor
        yn = y + h*s
        zn = z + h*j
        
        #Korektor
        y1 = y + h/2*(z + zn)
        z1 = z + h/2*(((-R*z-y/C)/L) + ((-R*zn-yn/C)/L))
        
        #Mempersiapkan iterasi selanjurnya+store hasil
        y = y1
        z = z1
        x += h
        A[0][i+1] = x
        A[1][i+1] = y1
        
        #Mencari nilai v untuk iterasi i+1 atau untuk t=(i+1)*0,002
        A[2][i+1] = A[0][i+1] * A[1][i+1] / C

    df = {'t' : A[0], 'I' : A[1], 'V_c' : A[2]}
    
    print("=============================")
    print("Hasil perhitungan Metode Heun\n")
    print(pandas.DataFrame(data = df))

if rules == "3":
    partisi = int(dt/h)
    A = [[0 for x in range(partisi + 1)] for y in range (3)]
    
    #Mengenai Nilai awal
    A[0][0] = x
    A[1][0] = y
    A[2][0] = x*y/C
    
    for i in range(0,partisi):
        # Mencari nilai k1-k4 dan l1-l4
        k1 = z
        l1 = (-R*z-y/C)/L
        k2 = (z+l1/2*h)
        l2 = (-R*(z+l1/2*h)-(y+k1/2*h)/C)/L 
        k3 = (z+l2/2*h)
        l3 = (-R*(z+l2/2*h)-(y+k2/2*h)/C)/L
        k4 = (z+l3*h)
        l4 = (-R*(z+l3*h)-(y+k3*h)/C)/L
    
        #Faktor penambah diiterasi adalah
        kh = (k1+ 2*k2 + 2*k3 + k4)/6*h #untuk fungsi f
        lh = (l1+ 2*l2 + 2*l3 + l4)/6*h
    
        #Nilai y dan z di iterasi berikutnya:
        yn = y + kh
        zn = z + lh
    
        #Mempersiapkan iterasi selanjurnya+store hasil
        x += h
        y = yn
        z = zn
        
        A[0][i+1] = x
        A[1][i+1] = yn
    
        #Mencari nilai v untuk iterasi i+1 atau untuk t=(i+1)*0,002
        A[2][i+1] = A[0][i+1] * A[1][i+1] / C

    df = {'t' : A[0], 'I' : A[1], 'V_c' : A[2]}
    
    print("===========================================")
    print("Hasil perhitungan Metode Runge Kutta Orde 4\n")
    print(pandas.DataFrame(data = df))