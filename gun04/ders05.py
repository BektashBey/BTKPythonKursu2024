# import time 
# print("merhaba dünya")
# time.sleep(5)
# print("sanada merhaba")


import datetime

a = input("birinci giriş")
giris = datetime.datetime.now()
print(giris)

b = input("ikinci giriş")
giris2 = datetime.datetime.now()
fark = giris2 - giris
print(fark)
print(fark.total_seconds())

