print("Program Menghitung Gaji Karyawan")
print("********************************\n")

gp = int(input("Masukkan Gaji Pokok = "))
print("\n")

mk = int(input("Masukkan Masa Kerja = "))
print("\n")

print("Pilih Status Kepegawaian")
print("========> 1. Pegawai Tetap")
print('          2. Pegawai Magang')
skp = int(input("Masukkan Pilihan = "))
print("\n")

print("Pilih Status Keluarga")
print('==========> 1. Sudah Berkeluarga')
print('            2. Belum Berkeluarga')
skg = int(input("Masukkan Pilihan = "))
print("\n")

if mk > 5:
    b = gp*15/100
else:
    b = 0

if skp == 1:
    ut = 50000
else:
    ut = 0

if skg == 1:
    t = gp*10/100
else:
    t = 0

gb = gp + b + ut + t

print("Gaji Bersih = Rp. ",gb)