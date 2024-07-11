sebze = ["domates", "biber"]
meyve = ["üzüm" ,"çilek" ,"kivi", "incir","armut","karpuz","ayva"]
sark = ["peynir","helva", "bal"]
yesillik = ["roka" , "maydonoz" ,"tere"]
pazar_listesi = [sebze,meyve,sark,yesillik ]

for x in range(len(pazar_listesi)):
    print(x+1,".katagorisi :",pazar_listesi[x])
    for y in range(len(pazar_listesi[x])):
        print(x+1,y+1,"ürünü\t",pazar_listesi[x][y])
