import numpy as np
from sympy import symbols

np.seterr(divide='ignore', invalid='ignore')

#CONSTANTS
h = 6.6256*(10**(-27))
c = 2.99792*(10**10)
k = 1.3805*(10**(-16))
pi = np.pi
exp = np.exp
T1 = 10
T2 = 100
T3 = 1000

#INPUT INTERVAL & JUMLAH PARTISI
a, b = map(int, input('Input Interval Panjang Gelombang (0,10): ').split(','))
n = int(input('Input Jumlah Partisi: '))
H = (b - a) / (n - 1)
dl = np.linspace(a, b, n)

#PERHITUNGAN
f_10 = (2*pi*h*(c**2)) / ((dl**(5))*(exp((h*c)/(k*dl*T1))-1))
f_100 = (2*pi*h*(c**2)) / ((dl**(5))*(exp((h*c)/(k*dl*T2))-1))
f_1000 = (2*pi*h*(c**2)) / ((dl**(5))*(exp((h*c)/(k*dl*T3))-1))

I_trap10 = (H/2)*(f_10[0] + 2 * sum(f_10[1:n-1]) + f_10[n-1])
err_trap10 = 2 - I_trap10

print("\nEnergi untuk T = 10K :", I_trap10)
print("Galat iterasi T = 10K :", err_trap10)

I_trap100 = (H/2)*(f_100[0] + 2 * sum(f_100[1:n-1]) + f_100[n-1])
err_trap100 = 2 - I_trap100
print("\nEnergi untuk T = 100K :", I_trap100)
print("Galat iterasi T = 100K :", err_trap100)

I_trap1000 = (H/2)*(f_1000[0] + 2 * sum(f_1000[1:n-1]) + f_1000[n-1])
err_trap1000 = 2 - I_trap1000
print("\nEnergi untuk T = 1000K :", I_trap1000)
print("Galat iterasi T = 1000K :", err_trap1000)