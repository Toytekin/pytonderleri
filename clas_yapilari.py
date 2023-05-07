class Arac():
    
    def __init__(self,marka='',model='',yakit='',yil='', fiyat=200):
        self.marka = marka
        self.model = model
        self.yakit = yakit    # Yazılımcı objelerinin özellikleri 
        self.yil = yil
        self.fiyat=fiyat
    def bilgilerigöster(self):
        print("""
        Araç Bilgisi:
        
        Marka :  {}
        
        Model : {}
        
        Yakit: {}
        
        Yil :  {}

        Fiyat: {}
        
        """.format(self.marka,self.model,self.yakit,self.yil, self.fiyat))

class Fonksiyonlar(Arac):
    def fiyatGuncelle(self,yeni_fiyat):
        self.fiyat=yeni_fiyat

    def modelGuncelle(self,yeni_model):
        self.model=yeni_model

    def yakitGuncelle(self, yeni_yakit_turu):
        self.yakit.appened(yeni_yakit_turu)




        
arac1=Fonksiyonlar('Toyoyo','Corolla',['Benzin'],'2012',200)
arac1.bilgilerigöster()
yebiFiyat=int(input('Yeni Fiyat Gir :'))
arac1.fiyatGuncelle(yebiFiyat)
yebiModel=input('Yeni Model Gir :')
arac1.modelGuncelle(yebiModel)
arac1.yakitGuncelle('deneme')

arac1.bilgilerigöster()




