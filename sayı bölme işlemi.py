sayı=int(input("bir sayı giriniz"))
while sayı>=0:
    if(sayı%3== 0 )and(sayı%5== 0):
        print("bölünüyor")
    else:
        print("bölünmüyor")
    sayı=int(input("bir sayı giriniz"))
