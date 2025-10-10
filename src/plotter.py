import matplotlib.pyplot as plt 

# Fungsi untuk membuat grafik populasi eksponensial
def gambar_grafik(t, P, P0, Pt, tahun, filename='../plots/gambar_grafik2.png'):
    plt.plot(t,P, marker='o')
    plt.title(f'Grafik Pertumbuhan Populasi Eksponential dari {P0:,} ke {Pt:,} dalam Periode {tahun} tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Populasi')
    plt.grid(True)
    plt.savefig(filename, bbox_inches = 'tight')
    plt.show()

# Fungsi untuk membuat grafik perbanfingan antara populasi eksponensial dan logistik
def bandingkan_model(t, P, P_log, K, tahun, filename='../plots/perbandingan.png'):
    plt.plot(t, P, 'r-o', label='Eksponential')
    plt.plot(t, P_log, 'b-s', label=f'Logistik (K ={K:,})')
    
    plt.title(f'Perbandingan Pertumbuhan Populasi dalam {tahun} tahun dengan model eksponensial dan logistik')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Populasi')
    plt.legend()
    plt.grid(True)

    plt.savefig(filename, bbox_inches='tight')
    plt.show()

