from itertools import zip_longest
import csv, json

def simpan_csv(t, P, P_log, r, K, filename='../data/data2.csv'):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([f'Laju Pertumbuhan (r): {r:.4f}'])
        writer.writerow([f'Carrying Capacity (K): {K if K else 'N/A'}'])
        writer.writerow(['Tahun','Populasi (Exponential)','Populasi (Logistic)'])

        for th,pop_exp,pop_log in zip_longest(t, P or [], P_log or []):
            formatted_exp = f'{round(pop_exp):,}'.replace(',','.') if pop_exp is not None else ''
            formatted_log = f'{round(pop_log):,}'.replace(',','.') if pop_log is not None else ''
            writer.writerow([th, formatted_exp, formatted_log])


def simpan_json(t, P, P_log, filename="../data/data2.json"):
    data = []

    for th, pop_exp, pop_log in zip_longest(t, P  or [], P_log or []):
        entry = {'Tahun' : int(th) }
        if pop_exp is not None:
            entry['Populasi (Exponential)'] = round(pop_exp)
        if pop_log is not None:
            entry['Populasi (Logistic)'] = round(pop_log)
        data.append(entry)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    
