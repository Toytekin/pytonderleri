class Hayvan:
    def __init__(self, ismi, yasi, cinsi):
        self.ismi = ismi
        self.yasi = yasi
        self.cinsi = cinsi

    def beslenme(self):
        print("Hayvan besleniyor...")

class Kopek(Hayvan):
    def __init__(self, ismi, yasi, cinsi, sadik=True):
        super().__init__(ismi, yasi, cinsi)
        self.sadik = sadik

    def havla(self):
        print("Hav! Hav!")

    def beslenme(self):
        print("Köpek mama yiyor...")

class Kus(Hayvan):
    def __init__(self, ismi, yasi, cinsi, kanat_uzunlugu):
        super().__init__(ismi, yasi, cinsi)
        self.kanat_uzunlugu = kanat_uzunlugu

    def uc(self):
        print("Kuş uçuyor...")
        print(f"Kuş Kanat uzunbluğu {self.kanat_uzunlugu}...")


    def beslenme(self):
        print("Kuş tohum yiyor...")

    def bilgiler(self):
        print(f'\n KUŞLAR\n \nİsmi: {self.ismi}\n Yaşı :{self.yasi}\n Cinsi :{self.cinsi}\n Kanat Uzunluğu :{self.kanat_uzunlugu}')   

class At(Hayvan):
    def __init__(self, ismi, yasi, cinsi, boyu):
        super().__init__(ismi, yasi, cinsi)
        self.boyu = boyu

    def kos(self):
        print("At koşuyor...")

    def beslenme(self):
        print("At ot yiyor...")


print('''

        OLUŞUM

''')
kopek=Kopek('Dog','23','Pibul')
kopek.havla()
kopek.beslenme()

kus=Kus('Bird',3,'Sparrow(Serçe)',45)
kus.uc()

at=At('Hourse','Midilli','Deneme','Boy :200 cm',)
at.kos()
kus2=Kus(cinsi='Cinsi', ismi='kuş2',yasi=25,kanat_uzunlugu=150)
kus2.bilgiler()
