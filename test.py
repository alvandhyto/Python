import numpy as np
from sympy import symbols
import math
from scipy.integrate import quad
from sympy import *

np.seterr(divide='ignore', invalid='ignore')

#CONSTANTS
h = 6.6256*(10**(-27))
c = 2.99792*(10**10)
k = 1.3805*(10**(-16))
pi = np.pi
exp = np.exp
inf = np.inf
T = [10, 100, 1000]
x = Symbol('x')


eksak_list = []
#INPUT JUMLAH PARTISI
dl_arr = []
interval = ([0, 10], [100, 110], [1000, 1010], [0, inf])
n = int(input("Input jumlah partisi: "))
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