
metin=input("Bir Cümle Yazınız:")
ara=input("Aranacak Kelimeyi Yazınız:")

ymetin = list(metin)

indis = metin.find(ara)
sonuc =""

if (indis-1) >= 0 :
	sonuc += ymetin[indis-1]
sonuc += ara
if (indis+len(ara)) <= len(ymetin) -1:
	sonuc += ymetin[indis+len(ara)]

print("Aradığınız kelimenin bir önceki ve bir sonraki değeri :", sonuc)