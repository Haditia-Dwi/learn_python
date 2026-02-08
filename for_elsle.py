# function else dapat digunakan untuk menghentikan break secara normal

huruf = input("Masukkan huruf: ")
huruf_dicari = input("Masukkan huruf yang ingin dicari: ")

for kata in huruf:
    if kata == huruf_dicari:
        print(f"Huruf yang anda cari berupa {huruf_dicari} ada ditemukan")
        break
    else:
        print(f"maaf, huruf {huruf_dicari}, tidak ditemukan didalamnya")