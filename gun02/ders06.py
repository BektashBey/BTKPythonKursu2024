# otoyol hız radar sistemi

yol = float(input("Yolu giriniz."))
zaman = float(input("Zamanı giriniz."))
hiz = yol/zaman

if hiz > 132:
    print(f"{hiz-132}kadar hız sınırını aştınız")

else:
    print("kurallara uyduğun için teşekkürler")



