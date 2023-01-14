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
interval = ([0, 10], [100, 110], [1000, 1010])
n = int(input('Input Jumlah Partisi: '))

for i in range(len(interval)):
    H = (interval[i][1] - interval[i][0]) / (n - 1)
    dl = np.linspace(interval[i][0], interval[i][1], n)
    dl_arr.append(dl)

#PERHITUNGAN ATURAN TRAPESIUM
f_arr = [[],[],[]]

for i in range(len(dl_arr)):
    for j in range(len(T)):
        f = (2*pi*h*(c**2)) / ((dl_arr[i]**(5))*(exp((h*c)/(k*dl_arr[i]*T[j]))-1))
        f_arr[i].append(f)

for i in range(len(dl_arr)):
    for j in range(len(f_arr)):
        I_trap = (H/2)*(f_arr[i][j][0] + 2 * sum(f_arr[i][j][1:n-1]) + f_arr[i][j][n-1])
        err_trap = 2 - I_trap

        print("\nEnergi untuk interval {} dan T = {:d}K: {}".format(str(interval[i]), T[j], I_trap))
        print("Galat iterasi interval {} dan T = {:d}K: {}".format(str(interval[i]), T[j], err_trap))