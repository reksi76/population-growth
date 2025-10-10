import tkinter as tk 
from tkinter import messagebox
import numpy as np
from calc import hitung_laju, hitung_populasi_eksponensial, hitung_populasi_logistik
from io_handler import simpan_csv, simpan_json
from plotter import gambar_grafik, bandingkan_model


def run_simulasi():
    try:
        P0 = int(entry_P0.get())
        Pt = int(entry_Pt.get())
        tahun = int(entry_tahun.get())
        model = var_model.get()
        mode = var_mode.get()
        K = entry_K.get()
        K = int(K) if K else None

        # pemanggilan fungsi fungsi perhitungan
        r = hitung_laju(P0, Pt, tahun)
        t = np.arange(0, tahun + 1, 1)
        P, P_log = None, None 

        # Pilih mode berdasarkan mode
        if model == 'eksponensial':
            P = hitung_populasi_eksponensial(P0, r, t)
            if mode in [1, 3]:
                gambar_grafik(t, P, P0, Pt, tahun)

        if model == 'logistic':
            if K == None:
                raise ValueError('Nilai K (carrying capacity diperlukan untuk menghitung populasi logistik)')

            P = hitung_populasi_eksponensial(P0, r, t)
            P_log = hitung_populasi_logistik(P0, r, K, t)
            if mode in [1, 3]:
                bandingkan_model(t, P, P_log, K, tahun)
            
        if mode in [2, 3]:
            simpan_csv(t, P, P_log,  r, K)
            simpan_json(t, P, P_log)

        messagebox.showinfo('Program Selesai','Data dan gambar grafik disimpan di folder data dan plots')

    except Exception as e:
        messagebox.showerror('Error', f'Terjadi kesalahan : {e}')


# GUI tkinter
root = tk.Tk()
root.geometry('450x300')
root.title('Population Growth Simulator')

# Input field
tk.Label(root, text='Populasi Awal (P0):').grid(row=0, column=0, sticky='w')
entry_P0 = tk.Entry(root)
entry_P0.grid(row=0, column=1)

tk.Label(root, text='Populasi Akhir (Pt):').grid(row=1, column= 0, sticky='w')
entry_Pt = tk.Entry(root)
entry_Pt.grid(row=1, column=1)

tk.Label(root, text='Jumlah tahun (t):').grid(row=2, column=0, sticky='w')
entry_tahun = tk.Entry(root)
entry_tahun.grid(row=2, column=1)

tk.Label(root, text='K (Carrying Capacity):').grid(row=3, column=0, sticky='w')
entry_K = tk.Entry(root)
entry_K.grid(row=3, column=1)

tk.Label(root, text='Model Pertumbuhan').grid(row=4, column=0, sticky='w', pady=10)
var_model = tk.StringVar(value='eksponensial')
tk.Radiobutton(root, text='Eksponensial',variable=var_model, value='eksponensial').grid(row=4,column=1, sticky='w')
tk.Radiobutton(root, text='Logistik', variable=var_model, value='logistic').grid(row=4, column=2, sticky='w')

# Pilihan mode (Radiobutton)

tk.Label(root, text='Mode Output: ').grid(row=5, column=0, sticky='w')
var_mode = tk.IntVar(value=3)
tk.Radiobutton(root, text='Grafik', variable=var_mode, value= 1).grid(row=5, column=1, sticky='w')
tk.Radiobutton(root, text='Simpan Data', variable=var_mode, value=2).grid(row=6, column=1, sticky='w')
tk.Radiobutton(root, text='Keduanya', variable=var_mode, value=3).grid(row=7, column=1, sticky='w')

# Tombol run 
btn_run = tk.Button(root, text='Jalankan Simulasi', command=run_simulasi)
btn_run.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()





