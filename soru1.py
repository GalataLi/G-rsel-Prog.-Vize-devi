email= input(str("Lütfen bir e-posta adresi giriniz: "))

for x in email:
    if (x=="@"):
        print("Bu bir e-posta adresidir. ")
        break
else:
    print("Bu bir e-posta adresi değildir.")