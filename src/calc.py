import numpy as np

def hitung_laju(Pt, P0, t):
    """ Hitung laju pertumbuhan """
    r  = 1/t * np.log(P0/Pt)
    return r

def hitung_populasi(P0, r, t):
    """Menghitung jumlah populasi tahunan dengan pertumbuhan eksponensial"""
    P = [P0 * np.exp(r*n) for n in t]
    return P 




