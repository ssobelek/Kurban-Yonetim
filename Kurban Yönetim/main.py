if __name__ == "__main__":
    class Kurban:

        def __init__(self, KurbanHissedari, KurbanKilo, PaySayisi):

            self.KurbanHissedari = KurbanHissedari
            self.KurbanKilo = KurbanKilo
            self.PaySayisi = PaySayisi

        def Kurban_listesi(self):
            print("""        Kurban Hissedarlarının isimleri : {}
            Kurbanın kilosu: {}
            Pay sayısı: {}\n""".format(self.KurbanHissedari, self.KurbanKilo, self.PaySayisi))

        def HissedarEkle(self, Hissedar):
            self.KurbanHissedari += Hissedar


    print("1. kurban bilgileri:")
    Kurban1 = Kurban("Sami Söbelek", 1110, 7)
    Kurban1.HissedarEkle(", İsmail Söbelek, AHmet G")
    Kurban1.Kurban_listesi()

    print("2. kurban bilgileri:")
    Kurban2 = Kurban("Mustafa Söbelek", 1200, 7)
    Kurban2.HissedarEkle(", Melek Söbelek")
    Kurban2.Kurban_listesi()
