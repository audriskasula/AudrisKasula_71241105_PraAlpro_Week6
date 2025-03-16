def hitung_ips(jumlah_matkul):
    total_bobot = 0
    total_sks = jumlah_matkul * 3
    
    for i in range(1, jumlah_matkul + 1):
        nilai = input(f"Nilai MK {i}: ")
        
        if nilai == "A" or nilai == "a":
            bobot = 4
        elif nilai == "B" or nilai == "b":
            bobot = 3
        elif nilai == "C" or nilai == "c":
            bobot = 2
        elif nilai == "D" or nilai == "d":
            bobot = 1
        else:
            bobot = 0
        
        total_bobot += bobot * 3
    
    ips = total_bobot / total_sks
    print(f"Nilai IPS anda semester ini {ips:.2f}")

print("Program penghitung IPS Mahasiswa")
jumlah = int(input("Berapa jumlah mata kuliah? "))
hitung_ips(jumlah)