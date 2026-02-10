# function else dapat digunakan untuk menghentikan break secara normal

kalimat = input("Masukkan kalimat kamu: ")
cari_kalimat = input("Masukkan kata yang ingin kamu cari: ")

for carka in kalimat:
    if carka == cari_kalimat:
        print(f"kata yang kamu cari ({cari_kalimat}) ada didalamnya")
        break
else:   # perlu diperhatikan bahwa "else" disini tidak boleh sejajar dengan if, karena nanti jatuhnya if else
        # yang tepat adalah "else" sejajar dengan for
    print(f"Maaf, kata yang kamu cari ({cari_kalimat}) tidak ada didalamnya")        
    
# kata = input("Masukkan kata: ")
# huruf_dicari = input("Masukkan huruf yang ingin dicari: ")
# kata = input("Masukkan kata: ")
# huruf_dicari = input("Masukkan huruf yang dicari: ")
    
# for huruf in kata:
#     if huruf == huruf_dicari:
#         print(f"huruf yang kamu cari ({huruf_dicari}) ada didalam kata tersebut")
#         break
#     else:
#         print(f"maaf huruf yang kamu cari ({huruf_dicari}) tidak ada didalam kata")
# for huruf in kata:
#     if huruf == huruf_dicari:
#         print("Huruf", huruf_dicari, "ada didalam kata")
#         break
#     else:
#         print ("Maaf,", huruf_dicari, "tidak ada didalam kata")
        
