#Penulisan Celcius harus = C
derajat = float(input("Berapa derajat cuaca ditempat anda sekarang : "))
suhu = (input("Dari jenis suhu : "))
suhu2 = (input("Ke dalam suhu : "))

if suhu == "C":
    result = derajat * 1.8 + 32
else:
    result = (derajat - 32) / 1.8
    
print(derajat, suhu, "dikonversikan", result, suhu2)