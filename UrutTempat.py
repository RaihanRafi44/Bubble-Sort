import pandas as pd #mengimpor modul panda dan mengalokasikan alias pd

def bubble_sort(data): # deklarasi fungsi bubble_sort yang mengambil parameter data
    n = len(data) # menyimpan jumlah elemen dari data yang diberikan

    for i in range(n - 1): #iterasi pertama
        for j in range(n - i - 1): #iterasi kedua
            if data[j][1] > data[j + 1][1]: #pembanding elemen kedua yaitu kolom tempat/venue dari pasangan elemen yang berdekatan, jika 
                #elemen kedua pertama lebih besar dari yang kedua maka akan di swap
                data[j], data[j + 1] = data[j + 1], data[j] #melakukan pertukaran elemen

# Membaca file Excel
dataframe = pd.read_excel('worldcup.xlsx')

# Mengambil kolom "Pertandingan" dan "Tempat"
pertandingan = dataframe['Pertandingan / Match'].tolist()
tempat = dataframe['Tempat / Venue'].tolist()

# Menggabungkan data pertandingan dan tempat ke dalam satu list
data = list(zip(pertandingan, tempat))

# Mengurutkan data berdasarkan tempat (dari awal ke akhir)
bubble_sort(data)

# Menampilkan hasil pengurutan pertandingan dan tempat
print("Hasil pengurutan berdasarkan tempat:")
for item in data:
    print(f"Pertandingan: {item[0]}, Tempat: {item[1]}")
