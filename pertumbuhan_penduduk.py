# Import library yang dibutuhkan
import numpy as np 
import matplotlib.pyplot as plt

# Input dari pengguna
P0 = int(input('Masukkan jumlah penduduk awal: '))         # Populasi awal
Pt = float(input('Masukkan jumlah penduduk setelah beberapa tahun: '))  # Populasi akhir
t = int(input('Masukkan jumlah tahun yang lewat: '))      # Jangka waktu (tahun)

# Validasi input agar nilai populasi > 0
if P0 <= 0 or Pt <= 0:
    raise ValueError('Nilai harus lebih besar dari 0')

# Hitung laju pertumbuhan tahunan (r) menggunakan rumus eksponensial
# Rumus: Pt = P0 * exp(r * t) → r = (1/t) * ln(Pt/P0)
r = 1 / t * np.log(Pt / P0) 

# Buat array tahun dari 0 sampai t
n = np.arange(0, t + 1, 1)

# Hitung populasi tiap tahun menggunakan rumus P = P0 * exp(r * n)
P = [P0 * np.exp(r * i) for i in n]

# Tampilkan laju pertumbuhan dan populasi tiap tahun
print(f'\nLaju pertumbuhan penduduk = {r:.4f}')
for value in P:
    print(value)

# Visualisasi pertumbuhan populasi
plt.plot(n, P, marker='o')
plt.title(f'Pertumbuhan Jumlah Penduduk dalam {t} Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk')
plt.grid(True)
plt.show()
