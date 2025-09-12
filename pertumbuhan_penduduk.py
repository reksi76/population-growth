import numpy as np 
import matplotlib.pyplot as plt

P0 = int(input('Masukkan jumlah penduduk awal: '))
Pt = float(input('Masukkan jumlah penduduk setelah beberapa tahun: '))
t = int(input('Masukkan jumlah tahun yang lewat: '))

if P0 <= 0 or Pt <=0:
	raise ValueError('Nilai harus lebih besar dari 0')

r = 1/(t) * np.log(Pt/P0) 

n = np.arange(0,t + 1,1)

P = [P0 * np.exp(r*i) for i in n]

print(f'\nLaju pertumbuhan penduduk = {r:.4f}')
for value in P:
	print(value)

plt.plot(n, P, marker='o')
plt.title(f'Pertumbuhan Jumlah Penduduk dalam {t} Tahun')
plt.grid(True)
plt.show()
	