import numpy as np

def hitung_laju(Pt, P0, t):
    """ Hitung laju pertumbuhan """
    return 1/t * np.log(P0/Pt)
    

def hitung_populasi_exponential(P0, r, t):
    """Menghitung jumlah populasi tahunan dengan pertumbuhan exponential"""
    return [P0 * np.exp(r*n) for n in t]

def hitung_populasi_logistic(P0, r, K, t):
    """Model pertumbuhan logistic"""
    return [K / (1 + ((K - P0) / P0 ) * np.exp(-r * m)) for m in t]
    




