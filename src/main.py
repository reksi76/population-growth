import os
import numpy as np 
import argparse
from calc import hitung_laju, hitung_populasi
from io_handler import simpan_csv,simpan_json
from plotter import gambar_grafik

def main():
    parser = argparse.ArgumentParser(description='Populaation Growth Simulator')
    parser.add_argument('--tahun', type=int, required= True, help='Jumlah tahun')
    parser.add_argument('--P0', type=int, required=True, help='Populasi Awal')
    parser.add_argument('--Pt', type=int, required=True, help='Populasi akhir')
    parser.add_argument('--mode', type=int, choices=[1,2,3], default=3, help='1:Grafik, 2:Simpan data, 3:Keduanya')
    
    args = parser.parse_args()

    for folder in ['data','plots']:
        os.makedirs(folder, exist_ok=True)

    r = hitung_laju(args.P0, args.Pt, args.tahun)
    t = np.arange(0, args.tahun + 1, 1)
    P = hitung_populasi(args.P0, r, t)

    if args.mode in [1,3]:
        simpan_csv(t, P, r)
        simpan_json(t, P)

    if args.mode in [2,3]:
        gambar_grafik(t, P, args.P0, args.Pt, args.tahun)

    print('Program Selesai. Data tersimpan di ../data, dan plot tersimpan di ../plots')

if __name__ == '__main__':
    main()

