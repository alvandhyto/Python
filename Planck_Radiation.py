import os
import numpy as np
from sympy import symbols
from time import sleep

np.seterr(divide='ignore', invalid='ignore')
os.system("cls")

#KONSTANTA
h = 6.6256*(10**(-27))
c = 2.99792*(10**10)
k = 1.3805*(10**(-16))
pi = np.pi
exp = np.exp
inf = np.inf
T = [10, 100, 1000]
interval = ([0, 10], [100, 110], [1000, 1010], [0, inf])

#PRINT CONSOLE UI
print("KALKULATOR ENERGI RADIASI")
print("1. Metode Aturan Trapesium")
print("2. Metode Aturan Simpson")
option = int(input("Input metode yang diinginkan: "))

#METODE ATURAN TRAPESIUM
if (option == 1):
    os.system("cls")
    print("KALKULATOR ENERGI RADIASI MENGGUNAKAN METODE TRAPESIUM")

    #INPUT JUMLAH PARTISI
    dl_arr = []

    n = int(input("\nInput jumlah partisi: "))
    for i in range(len(interval)):
        dl = np.linspace(interval[i][0], interval[i][1], n)
        dl_arr.append(dl)

    #PERHITUNGAN ATURAN TRAPESIUM
    f_arr = [[] for x in interval]
    print("\nHASIL PERHITUNGAN ATURAN TRAPESIUM")

    for i in range(len(interval)):
        for j in range(len(T)):
            f = (2*pi*h*(c**2)) / ((dl_arr[i]**(5))*(exp((h*c)/(k*dl_arr[i]*T[j]))-1))
            f_arr[i].append(f)

    for i in range(len(interval)):
        print("\nInterval \u03BB {}".format(str(interval[i])))
        
        for j in range(len(T)):
            H = (interval[i][1] - interval[i][0]) / (n - 1)
            I = (H/2)*(f_arr[i][j][0] + (2*sum(f_arr[i][j][1:n-1])) + f_arr[i][j][n-1])
            err = 2 - I

            print("\nEnergi untuk T = {:d}K: {}".format(T[j], I))
            print("Galat iterasi untuk T = {:d}K: {}".format(T[j], err))

#METODE ATURAN SIMPSON
elif (option == 2):
    os.system("cls")
    print("KALKULATOR ENERGI RADIASI MENGGUNAKAN METODE SIMPSON")

    #INPUT JUMLAH PARTISI
    dl_arr = []
    n = int(input("\nInput jumlah partisi: "))
    while (n % 2 != 0):
        print("Jumlah partisi harus merupakan bilangan genap!")
        n = int(input("Input jumlah partisi: "))

    #PERHITUNGAN ATURAN SIMPSON
    else:
        f_arr = [[] for x in interval]

        for i in range(len(interval)):
            dl = np.linspace(interval[i][0], interval[i][1], n)
            dl_arr.append(dl)

        print("\nHASIL PERHITUNGAN ATURAN SIMPSON")

        for i in range(len(interval)):
            for j in range(len(T)):
                f = (2*pi*h*(c**2)) / ((dl_arr[i]**(5))*(exp((h*c)/(k*dl_arr[i]*T[j]))-1))
                f_arr[i].append(f)

        for i in range(len(interval)):
            print("\nInterval \u03BB {}".format(str(interval[i])))
            
            for j in range(len(T)):
                H = (interval[i][1] - interval[i][0]) / (n - 1)
                I = (H/3)*(f_arr[i][j][0] + 2*sum(f_arr[i][j][:n-2:2]) + 4*sum(f_arr[i][j][1:n-1:2]) + f_arr[i][j][n-1])
                err = 2 - I

                print("\nEnergi untuk T = {:d}K: {}".format(T[j], I))
                print("Galat iterasi untuk T = {:d}K: {}".format(T[j], err))

else:
    print("Pilihan tidak terdapat di menu, silahkan ulangi.")