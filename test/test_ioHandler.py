import sys, os, csv, json
import numpy as np 
import pathlib as path 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from io_handler import simpan_csv, simpan_json

def test_simpan_csv(tmp_path):
    t = [0, 1, 2]
    P = [200, 210, 220]
    P_log = [210, 220, 230]
    r = 0.05
    K = 500

    test_file = tmp_path / 'data.csv'
    simpan_csv(t, P, P_log, r, K, filename=str(test_file))

    assert test_file.exists()

    with open(test_file) as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[2] == ['Tahun', 'Populasi (Exponential)', 'Populasi (Logistic)']
        assert int(rows[3][1].replace('.','')) == 200
        assert int(rows[3][2].replace('.','')) == 210

def test_simpan_json(tmp_path):
    t = [0, 1, 2]
    P = [200, 210, 220]
    P_log = [210, 220, 230]

    test_file = tmp_path / 'data.json'
    simpan_json(t, P, P_log, filename=str(test_file))
    assert test_file.exists()

    with open(test_file) as f:
        data = json.load(f)

    assert data[0]['Tahun'] == 0 
    assert data[0]['Populasi (Exponential)'] == 200
    assert data[0]['Populasi (Logistic)'] == 210
