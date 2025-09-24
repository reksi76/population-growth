import sys, os
import numpy as np 
from pathlib import Path 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from plotter import gambar_grafik

def test_gambar(tmp_path):
    t = np.arange(0,3)
    p = [100, 550, 1000]
    P0 = 100
    Pt = 1000
    tahun = 5

    plot_file = tmp_path / 'grafik.png'
    gambar_grafik(t, p, P0, Pt, tahun, filename = str(plot_file))

    assert plot_file.exists() 




