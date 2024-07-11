#bir yemek sipariş uygulaması

yemekSiparisi = input("yemek siparişinizi giriniz  :")
icecekSiparisi = input("içecek siparişinizi giriniz  :")

if yemekSiparisi == "pizza"  :
    
    if icecekSiparisi == "kola":
        print("evet doğru sipariş")

    else : 
        print(f"{yemekSiparisi} doğru ama ben {icecekSiparisi} söylemedim.")

else:
    print(f"ben {yemekSiparisi} ve {icecekSiparisi} söylemedim!")



