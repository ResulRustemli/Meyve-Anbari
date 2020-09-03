a = {"Alma":15,
    "Armut":5,
    "Yemis":4,
    "Banan":50,
    "Qarpiz":100,
    "Kivi":50}
mal_qiymeti={"Alma":0.9,
            "Armut":1.4,
            "Yemis":0.6,
            "Banan":1.5,
            "Qarpiz":0.2,
            "Kivi":1.7}

menü ="""
1 Mal elave et
2 Mal al
3 Mali Göster
4 Butun listi gör
5 Teze mal gir
6 Bir mali çıxar
7 Admin girişi
"""


def çıxar (mal:str,miqdar:int):
    a[mal]-=miqdar


def elave_et (mal:str,miqdar:int):
    a[mal]+=miqdar
    print("Elave olundu.")

def göster(mal):
    print(a[d])
şifre = "1234"
kasa=10000
while True:

    print(menü)
    seçim= input("Seçiminizi eliyin.")

    if seçim == "1":
        print("Meyveler:")

        for i in a:
            print(i)

        b = input("Hansi meyveni getirdin?")
        if b in a.keys():
            c = int(input(" Nece kilo getirdin?"))
            toplam_miqdar= a[b]+ c

            boş_yer = 5000 - a[b]
            if toplam_miqdar>5000:
                print("""
                Elimizde bu qeder boş yer yoxdur.
                Alabileceğimiz {} miqdari : {}""".format(b,boş_yer))
            else:
                if c*mal_qiymeti[b]< kasa:

                    kasa -= c * mal_qiymeti[b]

                    print("{} AZN alacaqsan.".format(c*mal_qiymeti[b]))
                    elave_et(b,c)
                else:
                    print("Elimizde bu qeder pul yoxdur")
                    print("{} manatimiz var".format(kasa))
        else:
            print("Bu maldan bizde yoxdur.")
    elif seçim =="2":
        print("Meyveler:")

        for i in a:
            print(i)

        b = input("Hansi meyveden alassan")
        if b in a.keys():
            c = int(input("Nece kilo alacaqsan?"))

            if c<=a[b]:
                kasa+= c*mal_qiymeti[b]
                print("{} Manat vereceksiniz.".format(c *mal_qiymeti[b]))
                çıxar(b,c)
            else:
                print("""
                Bizde yeterince {} yoxdur.
                Bizdeki {} miqdari : {} kg""".format(b,b,a[b]))
        else:
            print("Bu maldan bizde yoxdur.")

    elif seçim == "3":
        d = input("Hansi meyveni görmek istiyirsen?")
        if d in a.keys():
            print("""
            Bizde olan {} miqdari : {}
            Ceki qiymeti ise       : {}""".format(d,a[d],mal_qiymeti[d]))


        else:
            print("Bu maldan bizde yoxdur.")
    elif seçim =="4":
        x = 0
        for i in a.items():
            x += 1
            if x == 1:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 1:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 2:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 2:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 3:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 3:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 4:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 4:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 5:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 5:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 6:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 6:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 7:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 7:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 8:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 8:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 9:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 9:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))
            elif x == 10:
                y = 0
                for t in mal_qiymeti.items():
                    y += 1
                    if y == 10:
                        print("""
                        {:<15} ---- miqdari  : |{:^5}| qiymeti {}""".format(i[0], i[1], t[1]))

    elif seçim == "5":
        b = input("Hansi meyveyi gireceksiniz?")
        c = int(input("Nece kilo gireceksiniz?"))
        d = float(input("Ceki qiymetini yazın."))
        if c * d < kasa:
            kasa -= c * d

            print("{} Manat alacaxsiniz.".format(c * d))
            a[b]=c
            mal_qiymeti[b]=d
            z = 0
            for i in a:
                z += 1
                if z == 10:
                    print("""Bu mal ile depo dolub.
Başqa mal girebilmersiz""")


            print("Elave olundu.")
        else:
            print("Elimizde bu qeder pul yoxdu")
            print("{}  kg mal ala bilerik".format(kasa/d))


    elif seçim=="6":
        b=input("Hansi mali çıkarmaq istiyirsiniz?")
        a.pop(b)
        print("mal mufeffeqiyyetle çıkarıldı")
    elif seçim=="7":

        ş = input("Parol girin")
        if ş == şifre:
            altmenü = """
                    1 Kassadaki pullari gör
                    2 Parol değiştir."""
            print(altmenü)
            seç = input("Seçin")
            if seç =="1":

                print("Kassadaki pul miqdari : {}".format(kasa))

            elif seç =="2":

                şif=input("Kohne parolu girin")
                if şif == şifre:
                    şi=input("Teze parol girin")
                    şifre=şi
                else:
                    print("Xetali giris")

            else:
                print("Bele bir sey mumkun deyil.")
        else:
            print("Xetali giris")
    else:
        print("Bele bir sey mumkun deyil")
