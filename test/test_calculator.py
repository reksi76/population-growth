import sys
import os

# Memastikan agar test bisa dijalankan dari parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np 
from calc import hitung_laju, hitung_populasi_eksponensial, hitung_populasi_logistik

# Memeriksa apakah fungsi hitung_laju berjalan semestinya
def test_hitung_laju():
    P0, Pt, t = 100, 200, 10 
    r = hitung_laju(P0, Pt, t)
    expected = 1/t * np.log(Pt/P0)
    assert np.isclose(r, expected)

# Memastikan fungsi hitung_populasi berjalan semestinya
def test_hitung_populasi_eksponential():
    P0, r = 100, 0.05
    t = np.arange(0, 6, 1)
    P = hitung_populasi_eksponensial(P0, r, t)
    assert len(P) == len(t)
    assert np.isclose(P[0], P0)

    expected = P0 * np.exp(r * t[-1])
    assert np.isclose(P[-1], expected)

# Memastikan fungsi hitung_populasi_logistik berjalan semestinya
def test_hitung_populasi_logistik():
    P0, r, K = 100, 0.05, 1000
    t = np.arange(0, 6, 1)
    P = hitung_populasi_logistik(P0, r, K, t)
    assert len(P) == len(t)
    assert np.isclose(P[0], P0)

    expected = K / (1 + ((K - P0) / P0) * np.exp(-r * t[-1]))
    assert np.isclose(P[-1], expected)


