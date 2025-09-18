# Import library yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt
import csv
import json
import os

for folder in ['data', 'plots']:
    if not os.path.exists(folder):
        os.mkdirs(folder)

# Hitung laju pertumbuhan tahunan (r) menggunakan rumus eksponensial
# Rumus: Pt = P0 * exp(r * t) → r = (1/tahun) * ln(Pt/P0)
def hitung_laju(P0, Pt, tahun):
    r = 1/tahun * np.log(Pt/P0)
    return r

# Hitung populasi tiap tahun menggunakan rumus P = P0 * exp(r * n)
def hitung_populasi(P0, r, t):
    P = [P0 * np.exp(r*n) for n in t]
    return P

#Simpan data di csv
def simpan_csv(t, P, r):
    with open('data/data2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Kelajuan pertumbuhan (r)', f'{r}:.4f'])
        writer.writerow(['Tahun', 'Populasi'])
        for tahun,populasi in zip(t,P):
            formatted_population = f'{round(populasi):,}'.replace(',','.')
            writer.writerow([tahun, formatted_population])

#Simpan data dalam .json
def simpan_json(t, P):
    data = [{'tahun': int(th), 'populasi': round(pop)}
        for th, pop in zip(t,P)]

    with open('data/data2.json', 'w') as f:
        json.dump(data, f, indent=4)

# Visualisasi pertumbuhan populasi
def gambar_grafik(t, P, P0, Pt, tahun):
    plt.plot(t,P, marker='o')
    plt.title(f'Estimasi Pertumbuhan Penduduk dari {P0:,} ke {Pt:,} dalam {tahun} Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('jumlah Penduduk')
    plt.grid(True)
    plt.savefig('plots/grafik2.png') # simpan file di folder repo

    plt.show()

def main():
    try:
        tahun = int(input('Masukkan tahun: ')) # Jangka waktu
        P0 = int(input('Masukkan jumlah penduduk awal: ')) # Populasi awal
        Pt = int(input(f'Masukkan jumlah penduduk dalam periode {tahun}: '))  # Populasi akhir

        # Input P0 dan Pt harus > 0
        if P0 <= 0 or Pt <= 0: 
            raise ValueError('Nilai tidak bisa lebih kecil dari nol')
        #Pt harus lebih besar dari P0
        if Pt < P0:
            raise ValueError('Populasi akhir tidak boleh lebih kecil dari populasi awal')

        r = hitung_laju(P0, Pt, tahun)
        # Buat array tahun 
        t = np.arange(0, tahun + 1, 1)
        P = hitung_populasi(P0, r, t)

        mode = input('Pilih mode (1: Grafik, 2: Simpan data, 3: Keduanya): ')

        if mode in ['2', '3']:
            simpan_csv(t, P, r)
            simpan_json(t, P)

        if mode in ['1', '3']:
            gambar_grafik(t, P, P0, Pt, tahun)

        print('Program selesai. Data di simpan di folder data dan grafik di folder plots.')

    except ValueError as ve:
        print(f'Error : {ve}')
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')

if __name__ == '__main__':
    main()
