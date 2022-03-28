def garis() :
    print("=========================")

print("==== HOTEL KEMANGI 51=======")
print("KELAS didalam Hotel-- miskin-- menengah-- kaya ")
print("harga permalam --100.000/day --500.000/day --1.000.000/day")

kelas_hotel = input("masukkan kelas hotel anda :")
hari_bermalam = int(input("masukkan berapa lama anda bermalam :"))

if kelas_hotel == "miskin":
    if hari_bermalam <=2 :
        total_harga = 100000
    elif hari_bermalam <= 4 :
        total_harga = 400000
    else:
        total_harga = 900000       


elif kelas_hotel == "menegah":
    if hari_bermalam <=2 :
        total_harga = 50000*lama_inap
    elif hari_bermalam <= 4 :
        total_harga = 50000*lama_inap
    else:
        total_harga = 500000*lama_inap       


elif kelas_hotel == "kaya":
    if hari_bermalam <=2 :
        total_harga = 100000*lama_inap
    elif hari_bermalam <= 4 :
        total_harga = 100000*lama_inap
    else:
        total_harga = 100000*lama_inap       


garis()
print("Kamar yang dipilih : ",(kelas_hotel))
print("lama inap : ",(hari_bermalam))
print("Total Harga : ",(total_harga))





    

    
    
