# recursive fonksiyon ve iç içe fonksiyon tanımlanarak kullanımı 

def for_dongusu(baslangıc,bitis=0,artis=1):
    for_listesi = []
    def sirala(baslangıc,bitis,artis=artis):
        if baslangıc <= bitis:
            for_listesi.append(baslangıc)
            baslangıc += artis
            return sirala(baslangıc,bitis)
        return for_listesi
    if baslangıc > bitis:
        return sirala(bitis,baslangıc)
    else:
        return sirala(baslangıc,bitis)
print(for_dongusu(baslangıc=5 , bitis=10, artis=2))
