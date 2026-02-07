## PEMBAHASAN MENGENAI OPERATOR
## 1. OPERATOR ARITMATIKA:          seperti tambah,kurang.kali, dan bagi
## 2. OPERATOR PEMBAGIAN BULAT:     dengan menggunakan "//" akan membagi bilangan yang seharusnya desimal menjadi bulat
## 3. OPERATOR PEMBAGIAN MODULO:    dengan menggunakan "%" akan menampilkan sisa dari pembagiaan misal 10/3 hasilnya 1
## 4. OPERATOR PANGKAT:             dengan menggunakan tanda "**"

a = 10
b = 3

print(a+b)
print(a/b)
print(a%b)
print(a//b)

## PEMBAHASAN MENGENAI OPERATOR COMPOUND ASSIGNMENT
x = 15

x+= 20      ## operator ini berarti x = x+20
print(x)

x-= 20      ## operator ini berarti x = x-20
print(x)

x*= 20      ## opearator ini bearti x = x*20
print(x)

x/= 20      ## opearator ini bearti x = x/20
print(x)
## dan seterusnya tinggal menyesuaikan penghitungan apa yang ingin kita buat

## Operator Perbandingan
## digunakan untuk membandingkan dua hal yang hasilnya boolean benar atau salah
x = 80
y = 40

print(x>y)  #lebih besar:       true/false
print(x<y)  #lebih kecil:       true/false
print(x>=y) #lebih sama dengan: true/false
print(x<=y) #lebih kurang dari: true/false
print(x==y) #sama dengan:       true/false
print(x!=y) #tidak sama dengan: true/false

#OPERATOR LOGIKA
#digunakan untuk menggabungkan atau memodifikasi nilai boolean
# and(dan). menghasilkan True jika kedua kondisi True
# or(atau). menghasilkan True jika salah satu kondisi True
# not(tidak). membalik nilai boolean

umur = 25
print(umur > 18 and umur < 30)

bulan = "januari"
print(bulan == "januari" or bulan == "februari")

apakah_benar = True
print(not apakah_benar)

#OPERATOR STRING
# merupakan operator yang khusus bekerja untuk string saja
# Concatenation     (+)     digunakan untuk menambah string
# Repetition        (*)     mengulang string sejumlah angka
# Membership        (in)    mengecek apakah text ada didalam string