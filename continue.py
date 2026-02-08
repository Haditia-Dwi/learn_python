# penggunaan continue yaitu dengan menghiraukan perulangan saat ini dan dilanjutkan ke perulangan selanjutnya

for i in range(35):         # ulang i dalam range 35
    if i % 2 == 0:          # jika i dibagi habis 2 sama dengan 0
        continue            # function ini akan menghiraukan setiap bilangan yang habis dibagi 0
    else:
        print("angka", i)   # alhasil program akan mencetak bilangan bilangan ganjil saja