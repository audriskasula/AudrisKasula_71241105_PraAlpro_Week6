def fungsi(bil1, bil2):
    hasil = 0 
    print(f"{bil1} x {bil2} =", end=" ")
    for i in range(bil1):
        if i < bil1 - 1 :
            print(bil2, end=" + ")
        else : print(bil2, end=" = ")
        hasil += bil2
    print(f"{hasil}.")

fungsi(6, 5)
fungsi(7,10)
