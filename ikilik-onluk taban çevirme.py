
while True:
    print("1- iKiLiK TABANDAN ONLUK TABANA CEVIRME")
    print("2- ONLUK TABANDAN iKiLiK TABANA CEVIRME")
    print("3- CIKIS")
    secim = int(input("Yapmak istediginiz islemin numarasını girin:  "))

    if secim == 1:
        while True:
            ikiliks = input("İkilik tabandaki sayıyı girin: ")
            if set(ikiliks) <= set('01'):
                onluks = 0
                for i in range(len(ikiliks)):
                    onluks += int(ikiliks[i]) * 2 ** (
                            len(ikiliks) - 1 - i)     # İkilik sayıyı onluk sayıya dönüştürür.
                print("Onluk tabandaki karşılığı:", onluks)
                break
            else:
                print("Gecersiz giris ! Lütfen sadece 0 ve 1 girin.")

    elif secim == 2:
        onluks = int(input("Onluk tabandaki sayıyı girin: "))
        ikiliks = ''
        while onluks > 0:
            kalan = onluks % 2
            ikiliks = str(kalan) + ikiliks       # Onluk sayıyı ikilik sayıya dönüştürür.
            onluks = onluks // 2
        print("İkilik tabandaki karşılığı:", ikiliks)

    elif secim == 3:
        print("cevirici kapanıyor")
        break

    else:
        print("Gecersiz islem. Lütfen gecerli bir numara girin.")
