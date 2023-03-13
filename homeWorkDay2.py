
ogrenciler = ["Merve Pilavcı", "İsmail Öner", "Yağız Öner"]

ogrenciler.append(input("Öğrenci Adı Giriniz: "))
print(ogrenciler)

print("*********************************")


ogrenciAdiSoyadi = input("Silmek istediğiniz öğrencinin adını ve soyadını giriniz: ")

for ogrenci in ogrenciler:
    if ogrenciAdiSoyadi == ogrenci:
        ogrenciler.remove(ogrenci)
        print(f"{ogrenciAdiSoyadi} öğrencisi listeden silindi!")
        break
else:
    print(f"{ogrenciAdiSoyadi} isimli öğrenci listede bulunamadı.")


print("*********************************")


ogrenciler.extend(["Ayşe Duru", "Zeynep"])

print(ogrenciler)


print("******************************************")

for tekTek in ogrenciler:
    print(tekTek)


print("***********************")

ogrenciAdi = str(input("Numarasını öğrenmek istediğiniz öğrencinin adını ve soyadını giriniz:  "))

for ogrenci_No in ogrenciler:
    if ogrenciAdi == ogrenci_No:
        ogrenci_No = ogrenciler.index(ogrenci_No) + 1   #İlk öğrencinin numarası 0 yerine 1 olsun diye +1 ekledim.
        print("Öğrenci Numarası: ", ogrenci_No)
        break
else:
    print(f"{ogrenciAdi} isimli öğrenci listede bulunamadı.")


print("****************************************")

soru = int(input("Kaç adet öğrenci sileceksiniz ?: "))

i = 0

while i < soru:
    ogrenciSil = str(input("Silmek istediğiniz öğrencinin adını ve soyadını girin : "))
    ogrenciler.remove(ogrenciSil)
    i += 1
print(f"Liste güncel hali : {ogrenciler}")
