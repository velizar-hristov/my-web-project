# Basit bir hesap makinesi fonksiyonu tanımlayalım
def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    # Kullanıcıdan işlem seçmesini isteyelim
    secim = input("Lütfen bir işlem seçin (1/2/3/4): ")

    # Kullanıcıdan iki sayı alalım
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    # İşleme göre hesaplamayı yapalım ve sonucu gösterelim
    if secim == '1':
        print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif secim == '2':
        print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif secim == '3':
        print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif secim == '4':
        if sayi2 != 0:
            print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
        else:
            print("Hata: Bir sayı sıfıra bölünemez!")
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen 1, 2, 3 veya 4 girin.")

# Fonksiyonu çalıştır
hesap_makinesi()
