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
    print("""********************************************\nKurban Bilgileri...\n\n('İsim' 'Kurban kilosu' 'Hisse' 'Kurban no')""")
    for i in liste:
        print(i)
    print("********************************************")

def hissedarsil(hissedar):
    cursor.execute("DELETE FROM kurban WHERE Hissedarlar = (?) ", (hissedar,))
    con.commit()

def kurban_no_guncelle(eski,yeni):
    cursor.execute("UPDATE kurban set Kurbanno = ? where Kurbanno = ? ",(yeni,eski))
    con.commit()

def isim_guncelle(eski,yeni):
    cursor.execute("UPDATE kurban set Hissedarlar = ? where Hissedarlar = ? ",(yeni,eski))
    con.commit()
tablo()
Hissedarlar = input("İsminiz: ")
Kurbankilo = int(input("Kurbanın kilosu: "))
Hissesayisi = int(input("Hisse sayısı: "))
Kurbanno = int(input("Kurban numarası: "))
kurbanekle(Hissedarlar,Kurbankilo,Hissesayisi,Kurbanno)
hissedarekle()
hissedarsil()
kurban_no_guncelle(3,5)
isim_guncelle()
verilerial()
con.close()
