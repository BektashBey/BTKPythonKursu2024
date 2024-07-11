ad  = "mehmet"
ad2 = "ırmak"
ad3 = "umut"

print(ad +ad2 + ad3)
print(f"{ad} {ad2} {ad3}")

metin = "merhaba sayın {} kursumuza hoşgeldiniz."

print(metin.format(ad))
print(metin.format(ad2))
print(metin.format(ad3))

metin2 = "yarışmamızın başarı listesi {} {} {}"
print(metin2.format(ad,ad2,ad3))
print(metin2.format(ad2,ad3,ad))

metin3 = "{k1}, {k2} {k3} {k1},".format(k1=ad,k2=ad2,k3=ad3)
print(metin3)

