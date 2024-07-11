baslangıc = int(input("başlanngıç değeri"))
bitis = int(input("bitiş değeri"))
artis = int(input("artış değeri"))

toplam = 0
çarpım = 1
for i in range(baslangıc,bitis,artis):
    
    toplam += i
    çarpım *= i

print(toplam)
print(çarpım)  



