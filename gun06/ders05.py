# hata ayıklama 
try:
    a = int(input("enter a number:  "))

except:
    print("hata var")
else:
    print("değer atama işlemi başarıyla gerçekleşti")
finally:
    print("bende çalıştım")