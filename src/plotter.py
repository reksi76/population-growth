import matplotlib.pyplot as plt 

def gambar_grafik(t, p, P0, Pt, tahun, filename='../plots/gambar_grafik2.png'):
    plt.plot(t,p, marker='o')
    plt.title(f'Grafik Pertumbuhan Populasi dari {P0:,} ke {Pt:,} dalam Periode {tahun} tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Populasi')
    plt.grid(True)
    plt.savefig(filename)
    plt.show()
