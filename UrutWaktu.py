print ("----------WAKTU DARI AWAL KE AKHIR---------------")
import pandas as pd #mengimpor modul panda dan mengalokasikan alias pd

def bubble_sort(data): # deklarasi fungsi bubble_sort yang mengambil parameter data
    n = len(data) # menyimpan jumlah elemen dari data yang diberikan

    for i in range(n - 1):#iterasi pertama
        for j in range(n - i - 1):#iterasi kedua
            if data[j][1] > data[j + 1][1]:#pembanding elemen kedua yaitu kolom waktu/time dari pasangan elemen yang berdekatan, jika 
                #elemen kedua pertama lebih besar dari yang kedua maka akan di swap
                data[j], data[j + 1] = data[j + 1], data[j]

# Membaca file Excel
dataframe = pd.read_excel('worldcup.xlsx')

# Mengambil kolom "Pertandingan" dan "Waktu"
pertandingan = dataframe['Pertandingan / Match'].tolist()
waktu = dataframe['Waktu / Time'].tolist()

# Menggabungkan data pertandingan dan waktu ke dalam satu list
data = list(zip(pertandingan, waktu))

# Mengurutkan data berdasarkan waktu (dari awal ke akhir)
bubble_sort(data)

# Menampilkan hasil pengurutan pertandingan dan waktu
print("Hasil pengurutan berdasarkan waktu:")
for item in data: #melakukan iterasi melalui setiap elemen dalam data
    print(f"Pertandingan: {item[0]}, Waktu: {item[1]}") #mencetak hasil pengurutan, item[0] akan menampilkan
    #pertandingan, item[1] akan menampilkan waktu

print ("----------WAKTU DARI AKHIR KE AWAL---------------")

import pandas as pd

def bubble_sort(data):
    n = len(data)

    for i in range(n - 1): 
        for j in range(n - i - 1):
            if data[j][1] < data[j + 1][1]:  #pembanding elemen kedua yaitu kolom waktu/time dari pasangan elemen yang berdekatan, jika 
                #elemen pertama lebih kecil dari yang kedua maka akan di swap
                data[j], data[j + 1] = data[j + 1], data[j]

# Membaca file Excel
dataframe = pd.read_excel('worldcup.xlsx')

# Mengambil kolom "Pertandingan" dan "Waktu"
pertandingan = dataframe['Pertandingan / Match'].tolist()
waktu = dataframe['Waktu / Time'].tolist()

# Menggabungkan data pertandingan dan waktu ke dalam satu list
data = list(zip(pertandingan, waktu))

# Mengurutkan data berdasarkan waktu (dari akhir ke awal)
bubble_sort(data)

# Menampilkan hasil pengurutan pertandingan dan waktu
print("Hasil pengurutan berdasarkan waktu (dari akhir ke awal):")
for item in data:
    print(f"Pertandingan: {item[0]}, Waktu: {item[1]}")
