## PEMBAHASAN MENGENAI BREAK DAN CONTINUE
# break digunakan untuk mengentikan program perulangan
# sedangkan continue digunakan untuk melanjutkan ke perulangan berikutnya dengan menghentikan perulangan saat ini

tebak_angka = 95

while True:
    coba_tebak = int(input("Masukkan angka yang ingin anda tebak: "))
    
    if coba_tebak == tebak_angka:
        print("Selamat angka yang anda tebak benar..")
        break
        
    else:
        print("Maaf anda salah, Coba lagi!!")