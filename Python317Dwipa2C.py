print("Program Kalkulator")
print("******************\n")

b1 =  int(input("Masukkan Bilangan 1 = "))
b2 =  int(input("Masukkan Bilangan 2 = "))

print("Pilih Operasi")
print("=========> 1. Penjumlahan")
print("           2. Pengurangan")
print("           3. Perkalian")
print("           4. Pembagian")
pilihan = int(input("Masukkan Pilihan = "))

if pilihan == 1:
    print("Hasil Penjumlahan = ",b1+b2)
elif pilihan == 2:
    print("Hasil Pengurangan = ",b1-b2)
elif pilihan == 3:
    print("Hasil Perkalian = ",b1*b2)
elif pilihan == 4:
    print("Hasil Pembagian = ",b1/b2)
else:
    print("Pilihan Menu Tidak Ada")