import math
import os
import numpy as np
import warnings
from sympy import symbols
from scipy.special.orthogonal import p_roots
from scipy.integrate import quad
from sympy import *

#np.seterr(divide='ignore', invalid='ignore')
warnings.filterwarnings("ignore")
os.system("cls")

#KONSTANTA
i = 0
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
print("3. Metode Aturan Gauss-Legendre")
option = int(input("Input metode yang diinginkan: "))

#METODE ATURAN TRAPESIUM
if (option == 1):
    os.system("cls")
    print("KALKULATOR ENERGI RADIASI MENGGUNAKAN METODE TRAPESIUM")

    #INISIALISASI
    x = Symbol('x')
    eksak_list = []

    #INPUT JUMLAH PARTISI
    dl_arr = []
    n = int(input('\nInput jumlah partisi: '))

    for i in range(len(interval)):
        if i == 0:
            dl = np.linspace(interval[i][0], interval[i][1], n)
            def g(x):
                    return (2*pi*h*(c**2))/(x**5*(exp(h*c/k*x*T[i])-1))
            eksak = quad(g, interval[i][0], interval[i][1])[0]
            eksak_list.append(eksak)
        
        else:
            dl = np.linspace(interval[i][0], interval[i][1], n+1)
            
            if i == 3:
                dl = np.linspace(interval[i][0], interval[i][1], n)
                eksak_list.append(0)
                dl_arr.append(dl)
            
            else:
                def g(x):
                        return (2*pi*h*(c**2))/(x**5*(exp(h*c/k*x*T[i])-1))
                eksak = quad(g, interval[i][0], interval[i][1])[0]
                eksak_list.append(eksak)
        
        dl_arr.append(dl)

    #PERHITUNGAN ATURAN TRAPESIUM
    f_arr = [[] for x in interval]
    print("\nPERHITUNGAN ATURAN TRAPESIUM")

    for i in range(len(interval)):
        for j in range(len(T)):
            if interval[i][0] == 0:
                f = (2*pi*h*(c*2)) / ((dl_arr[i]**(5))*(exp((h*c)/(k*dl_arr[i]*T[j]))-1))
                
            else:
                f = (2*pi*h*(c*2)) / ((dl_arr[i][1:]**(5))*(exp((h*c)/(k*dl_arr[i][1:]*T[j]))-1))
            f_arr[i].append(f)

    for i in range(len(interval)):
        print("\nInterval \u03BB {}".format(str(interval[i])))
        
        for j in range(len(T)):
            if interval[i][0] == 0:
                H = (interval[i][1] - interval[i][0]) / (n - 1)
                I = (H/2)*(f_arr[i][j][0] + (2*sum(f_arr[i][j][1:n-1])) + f_arr[i][j][n-1])
        
            else:
                H = (interval[i][1] - interval[i][0]) / n
                I = (H/2)*(f_arr[i][j][0] + (2*sum(f_arr[i][j][1:])) + f_arr[i][j][n-1])
        
            err = eksak_list[j] - I
        
            if math. isnan(I) == True:
                I = 0
                err = eksak_list[j]

            print("\nEnergi untuk T = {:d}K: {}".format(T[j], I))
            print("Galat iterasi untuk T = {:d}K: {}".format(T[j], err))

#METODE ATURAN SIMPSON
elif (option == 2):
    os.system("cls")
    print("KALKULATOR ENERGI RADIASI MENGGUNAKAN METODE SIMPSON")

    #INISIALISASI
    x = Symbol('x')
    eksak_list = []
    dl_arr = []

    #INPUT JUMLAH PARTISI
    n = int(input("\nInput jumlah partisi: "))
    while (n % 2 != 0):
        print("Jumlah partisi harus merupakan bilangan genap!")
        n = int(input("Input jumlah partisi: "))

    #PERHITUNGAN ATURAN SIMPSON
    else:
        f_arr = [[] for x in interval]

        for i in range(len(interval)):
            if interval[i][1] < 99999999:
                def g(x):
                    return (2*pi*h*(c**2))/(x**5*(exp(h*c/k*x*T[i])-1))
          
                dl = np.linspace(interval[i][0], interval[i][1], n)
                eksak = quad(g, interval[i][0], interval[i][1])[0]
                eksak_list.append(eksak)
                dl_arr.append(dl)
          
            else:
                dl = np.linspace(interval[i][0], interval[i][1], n)
                eksak_list.append(0)
                dl_arr.append(dl)
        
        print("\nPERHITUNGAN ATURAN SIMPSON")

        for i in range(len(interval)):
            for j in range(len(T)):
                f = (2*pi*h*(c**2)) / ((dl_arr[i]**(5))*(exp((h*c)/(k*dl_arr[i]*T[j]))-1))
                f_arr[i].append(f)

        for i in range(len(interval)):
            print("\nInterval \u03BB {}".format(str(interval[i])))
            
            for j in range(len(T)):
                H = (interval[i][1] - interval[i][0]) / (n - 1)
                I = (H/3)*(f_arr[i][j][0] + 2*sum(f_arr[i][j][:n-2:2]) + 4*sum(f_arr[i][j][1:n-1:2]) + f_arr[i][j][n-1])
                err = eksak_list[j] - I
                
                if math. isnan(I) == True:
                    I = 0
                    err = eksak_list[j]

                print("\nEnergi untuk T = {:d}K: {}".format(T[j], I))
                print("Galat iterasi untuk T = {:d}K: {}".format(T[j], err))

#METODE ATURAN GAUSS-LEGENDRE
elif (option == 3):
    os.system("cls")
    print("KALKULATOR ENERGI RADIASI MENGGUNAKAN METODE GAUSS-LEGENDRE")

    def f(x):
        return (2*np.pi*h*(c**2))/(x**5*(np.exp(h*c/k*x*T)-1))
        
    n = int(input("\nInput jumlah titik interpolasi: "))

    print("\nHASIL PERHITUNGAN ATURAN GAUSS-LEGENDRE")

    for T in T:
        print("\n========")
        print('T: ', T)
        print("========")
        
        for a, b in [[0, 10], [100, 110], [1000, 1010], [0, inf]] :
            print(f"\nInterval ({a}, {b})")
            
            i += 1
            dl = np.linspace(a, b, n+1)
            [x, w] = p_roots(n+1)
            
            I = 0.5*(b-a)*sum(w*f(0.5*(b-a)*x+0.5*(b+a)))
            
            if i == 3:
                err = 0 - I
            
            else:
                err = quad(f, a, b)[0] - I
            
            if math.isnan(I) == True:
                    I = 0
                    err = 0 - I
            
            print('Nilai: ', I)
            print('Error: ', err)

else:
    print("Pilihan tidak terdapat di menu, silahkan ulangi.")