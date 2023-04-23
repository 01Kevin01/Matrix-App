import random

print("Hacker Simulasyonu")
print("-------------------")

while True:
    print("1- Bilgisayar hackle")
    print("2- Parola kır")
    print("3- Saldir")
    print("4- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        print("Bilgisayar hacklendi!")
    elif secim == "2":
        print("Parola kırıldı!")
    elif secim == "3":
        print("Saldırı gerçekleştiriliyor...")
        time.sleep(3)
        print("Saldırı başarılı!")
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim! Tekrar deneyin.")
