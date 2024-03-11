angka = int(input("Masukan angka yang ingin anda input : "))

if angka > 0 and angka %2 == 0:
    print(angka, "angka genap positif")
elif angka > 0 and angka %2 ==1:
    print(angka, "angka ganjil positif")
elif angka < 0 and angka %2 == 0:
    print(angka, "angka genap negatif")
elif angka < 0 and angka %2 == 1:
    print(angka, "angka ganjil negatif")
else:
    print(angka, "angka netral")    