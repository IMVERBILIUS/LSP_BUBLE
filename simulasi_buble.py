def garis() :
    print("==========================")

def ascending(mylist):
    mylist = sorted(mylist)
    return(mylist)

def descending(mylist) :
    mylist = sorted(mylist, reverse = True)
    return(mylist)

print ("Masukkan 3 buah nilai")

nilaiA = int(input("Masukkan Nilai A :"))
nilaiB = int(input("Masukkan Nilai B :"))
nilaiC = int(input("Masukkan Nilai C :"))
angka = [nilaiA, nilaiB, nilaiC]
garis()


def rata_rata(angka):
    return sum(angka)/len(angka)

print("Urutan Hasil Ascendiing")
print(ascending(angka))

print("Urutan Hasil descending")
print(descending(angka))

print("Angka Terbesar :",max(angka))

print("Rata-Rata Nilai :", rata_rata(angka))
