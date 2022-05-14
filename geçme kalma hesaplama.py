sayı1=int(input("not1 giriniz:"))
sayı2=int(input("not2 giriniz:"))
sözlü1=int(input("bir sayı giriniz:"))

ortalama=(int(sayı1)+int(sayı2)+int(sözlü1))/3
while ortalama:
    if ortalama>=50:
        print("geçtiniz")
    else:
        print("kaldınız")
    sayı1=int(input("not1 giriniz:"))
    sayı2=int(input("not2 giriniz:"))
    sözlü1=int(input("bir sayı giriniz:"))
