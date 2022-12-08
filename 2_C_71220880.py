angka = (input("Masukkan angka :"))
hitung = (input("Masukkan angka yg dihitung :"))
d = 0
for i in list(angka):
    if i == hitung:
        d = d+1
print("Angka",hitung ," muncul sebanyak" , d ,"kali.")
