# PERNYATAAN IF
# 1. pernyataan if digunakan untuk menjalankan kode hanya jika kondisi tertentu bernilai true
# 2. setelah if harus ada titik dua (:)
# 3. kode yang akan dijalankan jika kondisi True harus diindentasi(diberi spasi diawal)

# PERNYATAAN IF-ELSE
# digunakan jika ada dua kondisi yang memungkinkan untuk benar dan salah

# PERNYATAAN IF-ELIF
# digunakan jika ada lebih dari dua kondisi yang memungkinkan bernilai benar(bercabang)

# angka = int(input("Angka anda: "))

# if angka > 0:
#     print(f"angka yang anda masukkan adalah {angka} yang bernilai positif")
# elif angka < 0:
#     print(f"Angka yang anda masukkan adalah {angka} dan itu bernilai negatif")
# elif angka == 0:
#     print(f"angka yang anda masukkan adalah {angka} yang bernilai nol")
# else:
#     print("Hey, kamu memasukkan inputan yang tidak valid")\

# Program valdasi sim

umur_anda = int(input("Masukkan Umur Anda:"))
print("======== Program Validasi Sim ======")
print(f"Umur anda adalah {umur_anda} tahun")

if umur_anda < 17:
    print(f"Dengan umur {umur_anda} tahun tidak memungkinkan untuk kamu")
else:
    print(f"nah, kalo umur {umur_anda} tahun baru boleh")

