def ganjil(batas_bawah, batas_atas):
    
    if batas_bawah < batas_atas:
        print(f"bawah = {batas_bawah}, atas = {batas_atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya")
    else:
        print(f"bawah = {batas_bawah}, atas = {batas_atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya")
    
    print("adalah: ", end="")
    
    if batas_bawah < batas_atas:
        for i in range(batas_bawah, batas_atas + 1):
            if i % 2 == 1:
                print(i, end=", " if i + 2 <= batas_atas else "")
    else:
        for i in range(batas_bawah, batas_atas - 1, -1):
            if i % 2 == 1:
                print(i, end=", " if i - 2 >= batas_atas else "")
    
    print(".")

batasBawah = int(input("Masukkan batas bawah: "))
batasAtas = int(input("Masukkan batas atas: "))

ganjil(batasBawah, batasAtas)
