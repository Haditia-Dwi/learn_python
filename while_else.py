# penggunaan else juga dapat digunakan untuk menghentikan perulangan pada while

password_benar = "HaditiaJagoPython123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("Masukkan password kamu: ")
    percobaan += 1
    
    if password == password_benar:
        print("Password anda benar, silahkan tunggu untuk verifikasi")
        
    else:
        print("Maaf, password yang anda masukkan salah, sisa percobaan: ", max_percobaan-percobaan)
else:
    print("Maaf, anda sudah melebihi batas percobaan")