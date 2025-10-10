import numpy as np

def hitung_laju(P0, Pt, t):
    """ Hitung laju pertumbuhan """
    return 1/t * np.log(Pt/P0)
    

def hitung_populasi_eksponensial(P0, r, t):
    """Menghitung jumlah populasi tahunan dengan pertumbuhan eksponensial"""
    return [P0 * np.exp(r*n) for n in t]

def hitung_populasi_logistik(P0, r, K, t):
    """Model pertumbuhan logistik"""
    return [K / (1 + ((K - P0) / P0 ) * np.exp(-r * m)) for m in t]
    




