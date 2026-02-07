## konsep "variabel" bisa diartikan seperti kotak yang memiliki wadah
## Digunakan untuk menyimpan data saja
nama = "Haditia" ## variabel dengan nama "nama" yang berisi string
umur = 250 ## variabel yang berisi value "250" dengan tipe data integer
tinggi = 170.5 ## variabel yang berisi value "170.5" dengan tipe data float

## aturan penamaan variabel:
## 1. tidak boleh didahului tada "-"
## 2. tidak boleh dimulai dengan angka
## 3. tidak boleh menggunakan kata yang memiliki keyword di python seperti; "IF"
## 4. tidak boleh ada spasi dalam penamaan variabel


## Tipe data dasar di python
## 1. integer: bilangan bulat (1.2,3,4)
## 2. float: bilangan desiman (1,.. 2,..)
## 3. string: tipe data teks ("Hello World")
## 4. boolean: tipe data spesial yang hanya berisi true and false


## cara membuat string di python
## 1. diawali dengan petik satu '' atau petik dua ""
## 2. untuk membuat multi paragraf bisa menggunakan peti 2 tiga kali """"

biodata = """
aku adalah haditia dwi kusuma
yang lahir di Tasikmalayan"""

print(biodata)
print(type(biodata))

## tips, untuk mengubah variabel yang ada tetap menggunakan tanda "="
umurku = 12
print(umurku)

umurku = 20
print(umurku)