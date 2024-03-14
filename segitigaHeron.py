import math

sisiA = float(input("Input sisi A : "))
sisiB = float(input("Input sisi B : "))
sisiC = float(input("Input sisi C : "))

ABC = (sisiA+sisiB+sisiC)/2
heron = math.sqrt(ABC * (ABC - sisiA) * (ABC - sisiB) * (ABC - sisiC))

print("Hasil perhitungan memakai rumus segitiga heron adalah", heron)

keliling = sisiA + sisiB + sisiC
print("Keliling segitiga adalah", keliling)