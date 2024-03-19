print("=================================================================")
print("              Form pendaftaran organisasi                       ")
print("=================================================================")

jenisKelamin = input("Jenis kelamin (pria/wanita) : ").lower()
beratBadan = int(input("Berapa berat badan anda : "))
tinggiBadan = int(input("Berapa tinggi badan anda : "))
usia = int(input("Berapa usia anda : "))
cacat = input("Apakah anda memiliki cacat (y/n) : ").lower()
nilaiAkademis = int(input("Masukan nilai akademis anda : "))
skill = input("Apakah anda memiliki skill menembak, memanah, atau berkuda (y/n) : ").lower()

if cacat == "y":
    print("Anda tidak terima masuk ke organisasi X")
elif jenisKelamin == "wanita" and beratBadan >= 45 and beratBadan <= 50 and tinggiBadan >= 165 and usia < 20:
    print("Anda diterima masuk kedalam organisasi X")
elif jenisKelamin == "pria" and beratBadan <= 70 and tinggiBadan >= 170 and usia <= 25:
    print("Anda diterima masuk kedalam organisasi X")
elif jenisKelamin == "pria" or jenisKelamin == "wanita" and nilaiAkademis >= 90 and usia <= 30:
    print("Anda diterima masuk kedalam organisasi X")
elif jenisKelamin == "pria" or jenisKelamin == "wanita" and skill == "y":
    print("Anda diterima masuk kedalam organisasi X")
else:
    print("Anda tidak diterima masuk kedalam organisasi X")
