import sqlite3

con = sqlite3.connect("Kurban.db")
cursor = con.cursor()


def tablo():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS kurban (Hissedarlar TEXT, Kurbankilo INT, Hissesayisi INT, Kurbanno INT)")
    con.commit()


def kurbanekle(Hissedarlar, Kurbankilo, Hissesayisi, Kurbanno):
    cursor.execute("INSERT INTO kurban VALUES (?,?,?,?)", (Hissedarlar, Kurbankilo, Hissesayisi, Kurbanno))
    con.commit()


def verilerial():
    cursor.execute("SELECT * FROM kurban")
    liste = cursor.fetchall()
    print(
        """********************************************\nKurban Bilgileri...\n\n('İsim' 'Kurban kilosu' 'Hisse' 'Kurban no')""")
    for i in liste:
        print(i)
    print("********************************************")


def hissedarsil(hissedar):
    cursor.execute("DELETE FROM kurban WHERE Hissedarlar = (?) ", (hissedar,))
    con.commit()


def kurban_no_guncelle(eski, yeni):
    cursor.execute("UPDATE kurban set Kurbanno = ? where Kurbanno = ? ", (yeni, eski))
    con.commit()


def isim_guncelle(eski, yeni):
    cursor.execute("UPDATE kurban set Hissedarlar = ? where Hissedarlar = ? ", (yeni, eski))
    con.commit()


print(
    """
    ******************************************************************************************************
                               Kurban Yönetim Sistemine Hoşgeldiniz...  
    
                                    :YAPABİLECEĞİNİZ İŞLEMLER:                                          
    * q == Programı kapatmak için kullanınız.
    *kurbanekle = Hisse sahipleri, Kurbanın kilosu, Pay sayısı, Kurban numarasını içerir.
    *hissedarsil = Adını ve soyadını yazdıgınız hissedarın tüm bilgilerini siler.
    *kurbanno = Önce eski sonra yeni vermek istediğiniz kurban numarasını yazın ve değiştirin.
    *isimdeğiş = Önce değiştirmek istediğiniz sonra koymak istediğiniz ismi yazın ve değiştirin.
    *bilgilerigör = Bütün bilgileri gösterir.
    *islemler = Bu yazıyı tekrar görmek için kullanınız.
    ******************************************************************************************************
    """)
while True:
    s = input("İşlemi yazınız: ")

    if s == "q":
        print("\nSistem kapatılıyor...\n\n")
        break

    elif s == "islemler":
        print(
            """
            ******************************************************************************************************
                                       Kurban Yönetim Sistemine Hoşgeldiniz...  

                                            :YAPABİLECEĞİNİZ İŞLEMLER:                                          
            * q == Programı kapatmak için kullanınız.
            *kurbanekle = Hisse sahipleri, Kurbanın kilosu, Pay sayısı, Kurban numarasını içerir.
            *hissedarsil = Adını ve soyadını yazdıgınız hissedarın tüm bilgilerini siler.
            *kurbanno = Önce eski sonra yeni vermek istediğiniz kurban numarasını yazın ve değiştirin.
            *isimdeğiş = Önce değiştirmek istediğiniz sonra koymak istediğiniz ismi yazın ve değiştirin.
            *bilgilerigör = Bütün bilgileri gösterir.
            ******************************************************************************************************
            """)
        continue

    elif s == "hissedarsil":
        hissedar = input("Silinecek isimi tam yazınız: ")
        hissedarsil(hissedar)
        print("{} kullanıcısı silindi.".format(hissedar))
        continue

    elif s == "kurbanekle":
        Hissedarlar = input("Hissedar ismi: ")
        Kurbankilo = int(input("Kurbanın kilosu: "))
        Hissesayisi = int(input("Hisse sayısı: "))
        Kurbanno = int(input("Kurban numarası: "))
        kurbanekle(Hissedarlar, Kurbankilo, Hissesayisi, Kurbanno)
        print(verilerial())
        continue

    elif s == "isimdeğiş":
        eski = input("Değiştirmek istediğiniz ismi giriniz: ")
        yeni = input("Yeni ismi giriniz: ")
        isim_guncelle(eski, yeni)
        print("'{}' ismi '{}' olarak güncellendi".format(eski, yeni))
        continue

    elif s == "kurbanno":
        eski = input("Değiştirmek istediğiniz kurbanın numarasını giriniz: ")
        yeni = input("Yeni numarayı giriniz: ")
        kurban_no_guncelle(eski, yeni)
        print("'{}' numarası '{}' olarak güncellendi".format(eski, yeni))
        continue
    elif s == "bilgilerigör":
        print(verilerial())
        continue
    else:
        print("Lütfen komutu doğru girdiğinize emin olun.")
        continue
con.close()
