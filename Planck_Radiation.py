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

#INPUT INTERVAL & JUMLAH PARTISI
a, b = map(int, input('Input Interval Panjang Gelombang (0,10): ').split(','))
n = int(input('Input Jumlah Partisi: '))
H = (b - a) / (n - 1)
dl = np.linspace(a, b, n)

#PERHITUNGAN ATURAN TRAPESIUM
f_arr = []

for x in T:
    f = (2*pi*h*(c**2)) / ((dl**(5))*(exp((h*c)/(k*dl*x))-1))
    f_arr.append(f)

for y in range(len(f_arr)):
    I_trap = (H/2)*(f_arr[y][0] + 2 * sum(f_arr[y][1:n-1]) + f_arr[y][n-1])
    err_trap = 2 - I_trap

    print("\nEnergi untuk T = {:d}K: {}".format(T[y], I_trap))
    print("Galat iterasi T = {:d}K: {}".format(T[y], err_trap))