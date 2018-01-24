#memasukkan nama yang akan di cek gendernya
n = input('Nama: ')

#variabel di set 0
ce = co = 0

#pengecekkan karakter dari nama yang di masukkan
for char in n:
    if (char == "I" or char == "i"):
        ce += 1
    elif (char == "A" or char == "a"):
        ce += 1
    elif (char == "U" or char == "u"):
        ce += 1
    elif (char == "E" or char == "e"):
        ce += 1
    elif (char == "T" or char == "t"):
        ce += 1
    elif (char == "L" or char == "l"):
        ce += 1
    elif (char == "B" or char == "b"):
        co += 1
    elif (char == "D" or char == "d"):
        co += 1
    elif (char == "O" or char == "o"):
        co += 1
    elif (char ==" "):
        break


#perbandingan jumlah karakter pada nama, lalu akan muncul output nya apakah perempuan, lelaki atau tiak terdefinisi
if (ce > co):
    print("Perempuan")
elif (co > ce):
    print("Lelaki")
else:
    print("Tidak Terdefinisi Gendernya")


#hasil uji coba
#Adityo = Perempuan
#Gefry  = Perempuan
#Bram = Perempuan
#Fathan = Perempuan
#Erik = Perempuan
#Momo = Lelaki

#Dari beberapa nama yang saya masukkan hasilnya adalah 5 perempuan dan 1 laki-laki
#Karena karakter yang dicek untuk hasil perempuan lebih banyak dibanding karakter untuk laki-laki









