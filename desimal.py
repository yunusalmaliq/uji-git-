print (",,,,,,,,,,,,,,,,,,,,,,")
def option():
	print("")
	print("Angka Binary diawali 0b, Hexa diawali 0x, Oktal diawali 0o")
	print("---------------------------------------------------------\n")
	print("1.desimal ke biner")
	print("2.Desimal ke Hexa")
	print("3.Desimal ke Octal")
	print("4.Keluar")
	pilihan = int(input("masukan pilihan anda:"))
	return pilihan

pilihan = True
while(pilihan<4):
	pilihan = option()
	if pilihan ==1:
		print("---------------------------------------------------------")
		x = int(input("masukan angka biner:"))
		print("Angka desimal: ",des(x),2)
		print("---------------------------------------------------------\n")
	elif pilihan == 2:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Desimal: "))
		print (hex(x))
		print("---------------------------------------------------------\n")
	elif pilihan == 3:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Desimal: "))
		print (oct(x))
		print("---------------------------------------------------------\n")
	else:
		print("---------------------------------------------------------")
		print("good bye")