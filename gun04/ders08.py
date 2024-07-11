import os
dosya_adi = "gun04/deneme.txt"
with open(dosya_adi,"w") as dosya:
    dosya.write("esma")
with open(dosya_adi,"r") as dosya:
    print(dosya.read())

dosya_adi2 = "gun04/deneme.txt"
if not(os.path.isfile(dosya_adi2)):
    dosya = open(dosya_adi2,"x")
else:
    print("oluşturmak istediğiniz dosya mevcut")
    