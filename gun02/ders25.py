carpim = 1
adet = 0

while True:
    sayi = int(input("Bir sayı giriniz   :"))
    if sayi == 0 :
        print("Girilen sayıların çarpımı  :",carpim)
        continue
    carpim *= sayi
    adet += 1
    if adet == 10 :
        print("sayı girme işlemi tamamlanmıştır.")
        break
print(carpim)
   