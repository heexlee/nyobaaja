print("Program Menetukan Bilangan Terkecil")
print("***********************************")

a = int(input("Masukkan Bilangan ke-1 = "))
b = int(input("Masukkan Bilangan ke-2 = "))
c = int(input("Masukkan Bilangan ke-3 = "))

print("\n")
 
if(a < b) and (a < c):
    print("Bilangan ke-1 paling kecil")
elif(b < a) and (b < c):
    print("Bilangan ke-2 paling kecil")
elif(c < a) and (c < b):
    print("Bilangan ke-3 paling kecil")
else:
    print("Terdapat 2 atau 3 masukan/bilangan dengan nilai sama")