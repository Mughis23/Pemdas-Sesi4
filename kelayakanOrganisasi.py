print("              Form pendaftaran organisasi                       ")
print("=================================================================")

jenisKelamin = input("Jenis kelamin (pria/wanita) : ").lower()
beratBadan = int(input("Berapa berat badan anda : "))
tinggiBadan = int(input("Berapa tinggi badan anda : "))
usia = int(input("Berapa usia anda : "))
cacat = input("Apakah anda memiliki cacat (y/n) : ").lower()
nilaiAkademis = int(input("Masukan nilai akademis anda : "))
skill = input("Apakah anda memiliki skill menembak, memanah, atau berkuda (y/n) : ").lower()


if jenisKelamin == 'wanita':
    if beratBadan >= 45 and beratBadan <= 50 and tinggiBadan >= 165 and usia < 20 and cacat == 'n' and nilaiAkademis > 90 and skill == 'y':
        print("Anda berhak masuk kedalam organisasi")
    else:
        print("Anda tidak berhak masuk kedalam organisasi")
elif jenisKelamin == 'pria':
        if beratBadan <= 70 and tinggiBadan >= 170 and usia <= 25 and cacat == 'n' and nilaiAkademis > 90 and skill == 'y':
            print("Anda berhak masuk kedalam organisasi")
        else:
            print("Anda tidak berhak masuk kedalam organisasi")