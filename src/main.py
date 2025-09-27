import os
import numpy as np 
import argparse
from calc import hitung_laju, hitung_populasi_exponential, hitung_populasi_logistic
from io_handler import simpan_csv,simpan_json
from plotter import gambar_grafik,bandingkan_model 

def main():
    parser = argparse.ArgumentParser(description='Population Growth Simulator')
    parser.add_argument('--tahun', type=int, required= True, help='Jumlah tahun')
    parser.add_argument('--P0', type=int, required=True, help='Populasi Awal')
    parser.add_argument('--Pt', type=int, required=True, help='Populasi akhir')
    parser.add_argument('--model', type=str, choices=['exponential','logistic'],
                        default = 'exponential', help='Model Pertumbuhan Exponential atau Logistic')
    parser.add_argument('--K', type=int, default=None, help='carrying capacity (hanya untuk logistic)')
    parser.add_argument('--mode', type=int, choices=[1,2,3], default=3, help='1:Grafik, 2:Simpan data, 3:Keduanya')
    
    args = parser.parse_args()

    for folder in ['data','plots']:
        os.makedirs(folder, exist_ok=True)

    r = hitung_laju(args.P0, args.Pt, args.tahun)
    t = np.arange(0, args.tahun + 1, 1)
    P = None
    P_log = None

    if args.model == 'exponential':
        P = hitung_populasi_exponential(args.P0, r, t)
        if args.mode in [1,3]:
            gambar_grafik(t, P, args.P0, args.Pt, args.tahun)

    elif args.model == 'logistic':
        if args.K == None:
            raise ValueError('Nilai carrying capacity (K) diperlukan untuk menghitung populasi logistic')

        P = hitung_populasi_exponential(args.P0, r, t)
        P_log = hitung_populasi_logistic(args.P0, r, args.K, t)
        if args.mode in [1,3]:
            bandingkan_model(t, P, P_log, args.K, args.tahun)

    if args.mode in [2,3]:
        simpan_csv(t, P, P_log, r, args.K)
        simpan_json(t, P, P_log)

    print('Program Selesai. Data tersimpan di ../data, dan plot tersimpan di ../plots')

if __name__ == '__main__':
    main()

