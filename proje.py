from rehber import *

print("""

***********************************

1. rehberi göster

2. kişi sorgulama

3. kişi ekle

4. kişi sil

5. arama sayisi

q. çıkış

***********************

""")

rehber = Rehber()

while True:
    islem = input("Yapacğınız işlem: ")
    if (islem == "q"):
        print("Program sonlandırıldı.")
        break
    elif (islem == "1"):
        print("\n")
        rehber.show_rehber()
        print("\n")

    elif (islem == "2"):
        print("\n")
        isim = input("Hangi kişiyi görmek istiyorsunuz? ")
        print("Kişi sorgulanıyor..")
        rehber.search_person(isim)
        print("\n")

    elif (islem == '3'):
        print("\n")
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        telefon_numarasi = input("Telefon Numarası: ")
        yas = int(input("Yaş: "))
        arama_sayisi = int(input("Arama Sayısı: "))
        print("\n")

        yeni_kisi = Rehber_kaydi(isim, soyisim, telefon_numarasi, yas, arama_sayisi)
        print("Yeni kişi ekleniyor.")
        rehber.kisi_ekle(yeni_kisi)
        print("Kişi eklendi.")
        print("\n")

    elif (islem == '4'):
        print("\n")
        isim = input("Hangi kisiyi silmek istiyorsunuz? ")
        cevap = input("Emin misiniz ? (Y/N)")
        if (cevap == "Y"):
            print("Kisi siliniyor")
            rehber.kisi_silme(isim)
            print("Kişi Silindi.")
            print("\n")

    elif (islem == '5'):
        print("\n")
        isim = input("kimi aramak istiyorsunuz?")
        print("Arama sayınız arttı.")
        rehber.arama_sayisi_artma(isim)
        print("\n")

    else:
        print("\n")
        print("geçersiz işlem.")
        print("\n")