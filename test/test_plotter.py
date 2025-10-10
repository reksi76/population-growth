import sys, os
import numpy as np 
from pathlib import Path 

# Memastikan program test bisa berjalan dari parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from plotter import gambar_grafik, bandingkan_model

# Memeriksa apakah fungsi gambar_grafik berjalan semestinya
def test_gambar(tmp_path):
    t = np.arange(0,3)
    P = [100, 550, 1000]
    P0 = 100
    Pt = 1000
    tahun = 5

    plot_file = tmp_path / 'grafik.png'
    gambar_grafik(t, P, P0, Pt, tahun, filename = str(plot_file))

    assert plot_file.exists() 

# Memeriksa apakah fungsi bandingkan_model berjalan semestinya

def test_perbandingan(tmp_path):
    t = np.arange(0, 3, 1)
    P = [100, 500, 1000]
    P_log = [150, 650, 910]
    K = 900
    tahun = 3

    plot_file = tmp_path / 'gambar_perbandingan.png'
    bandingkan_model(t, P, P_log, K, tahun, filename=plot_file)

    assert plot_file.exists()






