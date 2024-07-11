sebze = ["domates", "biber"]
meyve = ["üzüm" ,"çilek" ,"kivi", "incir","armut","karpuz","ayva"]
sark = ["peynir","helva", "bal"]
yesillik = ["roka" , "maydonoz" ,"tere"]

# pazar_listesi = sebze + meyve + sark + yesillik
# print(pazar_listesi)

pazar_listesi = [sebze,meyve,sark,yesillik , "baklava"]
print(pazar_listesi)
# print(len(pazar_listesi))
# print(pazar_listesi[0])
# print(pazar_listesi[0][0])

for katagori in pazar_listesi:
    print(katagori)
    if type (katagori) != list:
        continue
    for urun in katagori:
        print(urun)







