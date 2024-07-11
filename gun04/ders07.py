dosya_adi = "gun04/deneme.txt"
with open(dosya_adi,"w") as dosya:
    dosya.write("esma")
with open(dosya_adi,"r") as dosya:
    print(dosya.read())

    