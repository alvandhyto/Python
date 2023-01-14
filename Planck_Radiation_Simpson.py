import numpy as np

a = 1000
b = 1010
n = int(input("Banyaknya partisi :"))
while (n % 2 != 0):
 print("Silakan masukkan angka genap")
 n = int(input("Banyaknya partisi :"))
else:
 h = (b - a) / (n - 1)
 x = np.linspace(a, b, n)
 f = np.sin(x)
 
 I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) + 4*sum(f[1:n-1:2]) + f[n-1])
 galat_simp = 2 - I_simp
 
 print(I_simp)
 print(galat_simp)