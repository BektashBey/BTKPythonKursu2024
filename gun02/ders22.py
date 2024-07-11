baslangıc = int(input("başlanngıç değeri"))
bitis = int(input("bitiş değeri"))
artis = int(input("artış değeri"))

if baslangıc > bitis:
    baslangıc, bitis = bitis , baslangıc

toplam = 0
carpım = 1

while baslangıc <= bitis:
    toplam += baslangıc
    carpım *= baslangıc
    baslangıc += artis

print(toplam)
print(carpım)  

metin = "Sayıların Toplamı {}, Çarpımı {}"
print(metin.format(toplam,carpım))