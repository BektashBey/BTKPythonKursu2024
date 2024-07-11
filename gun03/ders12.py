kume1 = {"a","b","c"}
kume2 = {1,2,3}
kume3 = kume1.union(kume2)
print(kume1,kume2,kume3)

kume4 = {"8",9,45}
kume3 = kume4 | kume2 | kume1
print(kume3)

# sayilar = set()
sayi = int(input("bir sayi giriniz"))
eb = sayi
ek = sayi
sayilar = {sayi}
while len(sayilar)<10:
    sayilar.add(int(input("Bir sayı giriniz")))
for ksayi in sayilar:
    if eb < ksayi:
        eb = ksayi
    if ek > ksayi:
        ek = ksayi
print("en büyük", eb)
print("en büçük", ek)

