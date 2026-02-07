##namamu = input('masukin namamu: ')

##print(f"Hai, kamu adalah: {namamu}")

## menggunakan fungsi len()
## fungsi len digunakan untuk mengecek karakter pada string
panjang_teks = "hei kamu haditia ya?"
print(len(panjang_teks))

## cara mengakses string dengan menggunakan indeksing
## pada pemrograman karakter dimulai dari indeks 0

nama = "haditia"
print(nama[0])

## penggunaan string slicing
## digunakan untuk mengambil sebagian data dalam karakter di string

buah = "semangka"
print(buah[4:6])


## penggunaan string methods
## ada beberapa fungsi yang bisa digunakan untuk memanipulasi string
## 1. .upper()                  untuk membuat karakter string menjadi huruf besar semua
## 2. .lower()                  untuk membuat karakter string menjadi huruf kecil semua
## 3. .title()                  untuk mengubah setiap awal karakter dikata pada string menjadi huruf besar
## 4. .capitalize()             untuk mengubah awal karakter menjadi huruf besar 
## 5. .strip()                  untuk menghilangkan karakter kosong seperti spasi di awal 
## 6. .replace(dari, menjadi)   untuk mengganti bagian tertentu dalam string
## 7. .count(text)              untuk menghitung beberapa kali text muncul
## 8. .find(text)               untuk mencari posisi text muncul

someone = "jokowi"

print(someone)
print(someone.upper())
print(someone.title())
print(someone.replace("wi", 'mullet'))

## penggunaan escape character
## \n: digunakan untuk membuat new line atau enter
## \t: digunakan untuk membuat tab
## \ : digunakan untuk membuat backslash

contoh = "hey aku haditia \n umurku 20 tahun"
kalimatnya = "alamat:\tjalan arjuna\nrumah:\twarna pink"
kalimat = "tiba-tiba mereka \"merusak\" kepada saya"

## STRING INTERPOLATION
## merupakan cara untuk menggabungkan variabel dengan teks
## penggunaannya cukup tambahkan huruf "f" diawal yang artinya f-strings

nama = "Haditia"
alamat = "bulak pacing"
rumah = 20

biodata = f"hei, nama saya {nama} yang beralamat di {alamat} dan nomor rumahnya adalah {20}"
print(biodata)
