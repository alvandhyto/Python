import numpy as np
from sympy import symbols

np.seterr(divide='ignore', invalid='ignore')

#CONSTANTS
h = 6.6256*(10**(-27))
c = 2.99792*(10**10)
k = 1.3805*(10**(-16))
pi = np.pi
exp = np.exp
T = [10, 100, 1000]

#INPUT JUMLAH PARTISI
dl_arr = []
interval = ([0, 10], [100, 110], [1000, 1010], [0, np.inf])
n = int(input("Input jumlah partisi: "))
while (n % 2 != 0):
    print("Jumlah partisi harus merupakan bilangan genap!")
    n = int(input("Input jumlah partisi: "))

#PERHITUNGAN ATURAN SIMPSON
else:
    f_arr = [[] for x in interval]

    for i in range(len(interval)):
        dl = np.linspace(interval[i][0], interval[i][1], n)
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
            err = 2 - I

            print("\nEnergi untuk T = {:d}K: {}".format(T[j], I))
            print("Galat iterasi untuk T = {:d}K: {}".format(T[j], err))