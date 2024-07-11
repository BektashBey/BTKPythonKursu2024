# oop giriş
class ogrenci():
    pass

ogrenci1 = ogrenci

ogrenci1.ad = "kerim"
ogrenci1.soyad = "karakan"

print(ogrenci1,ogrenci1.ad,ogrenci1.soyad)

ogrenci2 = ogrenci()

ogrenci2.ad = "ege"
ogrenci2.soyad = "altun"

print(ogrenci2,ogrenci2.ad,ogrenci2.soyad)

print(type(ogrenci2))