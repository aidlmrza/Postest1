import math


print ("Login dulu coy")
username = input ("Masukkan nama        : ")
password = input ("Masukkan Password    : ")


print (f"Halo {username}, Selamat Datang di Kalkulator Volume Bangun ruang")
print ("="*30)
print ("""PILIH BANGUN RUANG
    1. Bola
    2. Tabung
    3. Limas Segitiga""")
print ("="*30)
bangun = int (input("pilih bangun ruang dengan memasukkan angka = "))
print ("="*30)
pi = math.pi
if bangun == 1:
    print ("Menghitung Volume Bola")
    jari_jari = float (input("Masukkan jari-jari = "))
    if jari_jari < 1:
        print ("jari-jari harus lebih dari 1 coy")
    else:
        V_Bola = 4/3 * pi * jari_jari**3
        print (f"Volume Bolanya adalah {V_Bola}")
elif bangun == 2:
    print ("Menghitung Volume Tabung")
    jari_jari = float (input("Masukkan jari-jari = "))
    tinggi = float (input("Masukkan tinggi = "))
    if jari_jari < 1 or tinggi < 1:
        print ("jari-jari sama tinggi ga boleh kurang dari 1 coy")
    else:
        V_Tabung = pi * jari_jari**2 * tinggi
        print (f"Volume tabungnya adalah {V_Tabung}")
elif bangun == 3:
    print ("Menghitung Volume Limas Segitiga")
    luas_alas = float (input("Masukkan luas alas = " ))
    tinggi = float (input("Masukkan tinggi = "))
    if luas_alas < 1 or tinggi < 1:
        print ("luas alas sama tinggi ga boleh kurang dari 1 coy")
    else:
        V_LimasSegitiga = 1/3 * luas_alas * tinggi
        print (f"Volume Limas Segitiganya adalah {V_LimasSegitiga}")
else:
    print("hanya ada 3 pilihan")
