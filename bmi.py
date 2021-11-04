print("Body Mass Index\n")

berat_badan = int(input("Masukkan Berat Badan: "))
tinggi_badan = int(input("Masukkan Tinggi Badan: "))

bmi = berat_badan/(tinggi_badan*tinggi_badan)

if bmi < 18.5:
	print("Kategori : kurus")
elif bmi < 25:
	print("Kategori : Normal")
elif bmi < 30:
	print("Kategori : Kelebihan berat")
else:
	print("Kategori : Kegemukan")