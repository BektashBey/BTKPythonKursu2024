# kalıtım kavramı 

class Ogrenci():
    def __init__(self,ad,soyad):
        self.ad = ad 
        self.soyad = soyad

class FOgrenci(Ogrenci):
    def __init__(self, ad, soyad, fakulte):
        super().__init__(ad, soyad)
        self.fakulte = fakulte

class BOgrenci(FOgrenci):
    def __init__(self, ad, soyad, fakulte,bolum):
        FOgrenci.__init__(self,ad,soyad,fakulte)
        self.bolum = bolum

ogrenci = Ogrenci(ad = "sakir", soyad= "can")
fogrenci = FOgrenci(ad= "sakir", soyad="can", fakulte="mühendislik")
bogrenci = BOgrenci(ad= "sakir", soyad="can", fakulte="mühendislik" ,bolum="yazılım")

print(vars(ogrenci))
print(vars(fogrenci))
print(vars(bogrenci))

