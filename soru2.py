URL =input("Bir URL adresi giriniz : ").split(".")

if URL[0] == "www" and URL[2] == "com" :


    print("adres doğrulandı")

else :
    print('adres hatalı')