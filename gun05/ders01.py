def factorial(num):
    if num <0 :
        return "hatalı sayı girişi"
    # raise ValueError("hatalı giriş yapıldı.")
   
    if num > 0 :
        return num * factorial(num -1)
    else:
        return 1
    
print(factorial(-9))

