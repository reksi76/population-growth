import csv, json

def simpan_csv(t, P, r, filename='../data/data2.csv'):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([f'Laju Pertumbuhan (r): {r:.4f}'])
        writer.writerow(['Tahun','Populasi'])
        for th,pop in zip(t,P):
            formatted = f'{round(pop):,}'.replace(',','.') 
            writer.writerow([th,formatted])

def simpan_json(t, P, filename="../data/data2.jsom"):
    data = [{'Tahun': int(n),'Populasi': round(m)} for n,m in zip(t, P)]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    
