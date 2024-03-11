angka1 = int(input("Masukan angka pertama : "))
angka2 = int(input("Masukan angka kedua : "))
angka3 = int(input("Masukan angka ketiga : "))

if angka1 > angka2 and angka1 > angka3:
    print(angka1, "lebih besar dari", angka2, "dan" ,angka3 )
elif angka2 > angka1 and angka2 > angka3:
    print(angka2, "lebih besar dari", angka1, "dan", angka3)
elif angka3 > angka1 and angka3 > angka2:
    print(angka3, "lebih besar dari", angka1, "dan", angka2)
          
elif angka1 == angka2 and angka1 and angka2 > angka3:
    print(angka1, "lebih besar dari", angka3)
elif angka1 == angka3 and angka1 and angka3 > angka2:
    print(angka3, "lebih besar dari", angka2)
elif angka2 == angka3 and angka2 and angka3 > angka1:
    print(angka2, "lebih besar dari", angka1)
    
else:
    print(angka1, angka2, "dan", angka3,"sama besar")