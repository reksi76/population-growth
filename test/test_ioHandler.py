import sys, os, csv, json
import numpy as np 
import pathlib as path 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from io_handler import simpan_csv, simpan_json

def test_simpan_csv(tmp_path):
    t = [0, 1, 2]
    P = [200, 210, 220]
    r = 0.05

    test_file = tmp_path / 'data.csv'
    simpan_csv(t, P, r, filename=str(test_file))

    assert test_file.exists()

    with open(test_file) as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[1] == ['Tahun', 'Populasi']
        assert int(rows[2][1].replace('.','')) == 200

def test_simpan_json(tmp_path):
    t = [0, 1, 2]
    P = [200, 210, 220]

    test_file = tmp_path / 'data.json'
    simpan_json(t, P, filename=str(test_file))
    assert test_file.exists()

    with open(test_file) as f:
        data = json.load(f)

    assert data[0]['Tahun'] == 0 
    assert data[0]['Populasi'] == 200
