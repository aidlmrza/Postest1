import math

print ("Register dulu ya")
Nama_daftar = str(input("Nama     : "))
NIM_daftar = int(input("NIM      : "))
print ("="*30)
print ("Login dulu coy")
Nama_login = str(input("Nama     : "))
NIM_login = int(input("NIM      : "))

if Nama_daftar != Nama_login or NIM_daftar != NIM_login:
    print ("Nama atau NIM anda salah")
else:
    print ("Akun anda benar")
    print ("="*30)
    print (f"Halo {Nama_daftar}, Selamat Datang di Kalkulator Volume Bangun ruang")
    print ("="*30)
    print ("""PILIH BANGUN RUANG
    1. Bola
    2. Tabung
    3. Limas Segitiga""")
    print ("="*30)
    bangun = int (input("Pilih bangun ruang dengan memasukkan angka = "))
    print ("="*30)
    pi = math.pi
    if bangun == 1:
        print ("Menghitung Volume Bola")
        jari_jari = float (input("Masukkan jari-jari = "))
        if jari_jari < 1:
            print ("jari-jari harus lebih dari 0 coy")
        else:
            V_Bola = 4/3 * pi * jari_jari**3
            print (f"Volume Bolanya adalah {V_Bola:.2f}")
    elif bangun == 2:
        print ("Menghitung Volume Tabung")
        jari_jari = float (input("Masukkan jari-jari = "))
        tinggi = float (input("Masukkan tinggi = "))
        if jari_jari < 1 or tinggi < 1:
            print ("Jari-jari sama tinggi ga boleh kurang dari 1 coy")
        else:
            V_Tabung = pi * jari_jari**2 * tinggi
            print (f"Volume tabungnya adalah {V_Tabung:.2f}")
    elif bangun == 3:
        print ("Menghitung Volume Limas Segitiga")
        luas_alas = float (input("Masukkan luas alas = " ))
        tinggi = float (input("Masukkan tinggi = "))
        if luas_alas < 1 or tinggi < 1:
            print ("Luas alas sama tinggi ga boleh kurang dari 1 coy")
        else:
            V_LimasSegitiga = 1/3 * luas_alas * tinggi
            print (f"Volume Limas Segitiganya adalah {V_LimasSegitiga:.2f}")
    else:
        print("Hanya ada 3 pilihan bangun ruang")
