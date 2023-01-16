import time

print("Written by Hüseyin Berk Keskin")

hesap_bakiyesi = 1000

def para_yatir(para):
    global hesap_bakiyesi
    while True:
        print("Hesabiniza {} TL yatirilacaktir, onayliyor musunuz?".format(para))
        print('1. Onayla')
        print('2. İptal et')
        onay = int(input('Seçimiciz: '))
 
        if onay==1:
            hesap_bakiyesi = hesap_bakiyesi + para
            time.sleep(2)
            print("Hesap bakiyesi güncellenmiştir. Yeni bakiyeniz {}".format(hesap_bakiyesi))
            print("Üst menüye yönlendiriliyorsunuz")
            time.sleep(2)
            return False
        elif onay==2:
            print("Hesaba para yatirma işleminiz iptal edilmiştir. Üst menüye yönlendiriliyorsunuz")
            time.sleep(2)
            return False
        else:
            print("Yanliş seçim yaptiniz. Lütfen tekrar deneyiniz")
            time.sleep(2)

def para_cek(para):
    global hesap_bakiyesi
    while True:
        if hesap_bakiyesi >= para:
            print("Hesabinizdan {} TL çekilecektir, onayliyor musunuz?".format(para))
            print('1. Onayla')
            print('2. İptal et')
            sec = int(input('Seçimiciz: '))

            if sec==1:
                hesap_bakiyesi = hesap_bakiyesi - para
                time.sleep(2)
                print("Hesap bakiyesi güncellenmişntir. Kalan bakiyeniz {}".format(hesap_bakiyesi))
                time.sleep(2)
                return False
            elif sec==2:
                print("Hesaba para çekme işleminiz iptal edilmiştir. Üst menüye yönlendiriliyorsunuz")
                time.sleep(2)
                return False
            else:
                print("Yanliş seçim yaptiniz. Lütfen tekrar deneyiniz")
                time.sleep(1)
        else:
            print('Çekmek istediğiniz tutar hesap bakiyenizden fazla olduğu için işlem gerçekleştirilemiyor')
            time.sleep(1)
            break

print("Lütfen kartinizi yerleştiriniz")
time.sleep(3)
sifre = [6131]
sifre_girdisi = int(input("Lütfen şifrenizi giriniz: "))

while True:
    if sifre_girdisi in sifre:
        print("Hesabinizda {} TL bulunmaktadir".format(hesap_bakiyesi))
        print("1. Para yatir")
        print("2. Para çek")
        print("3. Kart iade")
        secim = input("Seçiminiz: ")

        if secim==1 or secim=='1' or secim=="1. Para yatir" or secim=="Para yatir":
            para = int(input('Yatirilacak tutar: '))
            print(para_yatir(para))

        elif secim==2 or secim=='2' or secim=="2. Para çek" or secim=="Para çek":
            para = int(input('Çekilecek tutar: '))
            print(para_cek(para))

        elif secim==3 or secim=='3' or secim=='3. Kart iade' or secim=='kart iade':
            print('Kartiniz iade ediliyor. İyi günler dileriz...')
            time.sleep(1)
            break
        else:
            print("Hatali tuşlama yaptiniz, lütfen tekrar deneyiniz")
            time.sleep(1.5)
            pass
    elif not sifre_girdisi in sifre:
        print("Hatali şifre girişi yaptiniz")
        print("Kartiniz iade ediliyor")
        time.sleep(1.5)
        break
        
