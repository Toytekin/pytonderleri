#Listeleri değiştiren metotlar dışında aynı

demet=('Sarı','Yeşil','Kırmızı','Mavi','Lacivert')


#! Kümeler  MAP

# kumeler={'Sarı','Yeşil','Kırmızı','Mavi','Lacivert'}
# print(kumeler)

#! Elemen ekleme
# kumeler.add('Pembe')
# print(kumeler)

#! Elemen silme
# kumeler.remove('Yeşil')
# print(kumeler)

# kumeler.discard('Beyazlık') # ?  remove dan farkı silinecek öge yoksa hata vermez, varsa siler.
# print(kumeler)
 


 #! Kümelrede kesişim ve birleşim işlemleri

kume1={'Sarı','Yeşil','Kırmızı','Mavi','Lacivert'}
kume2={'Sarı','Siyah','Kırmızı','Mavi','Pembe'}

print(kume1.intersection(kume2))  #? iki kümenin kesişimini bize verir
print(kume1.union(kume2))         #?  iki kümenin birleşimi (bir ürünü 1 defa yazar)
print(kume1.difference(kume2))    #?  kume1 de olan ama kume2 de olmayan elemanları getirir
print(kume2.difference(kume1))    #? kume2 de olan ama kume1 de omayan elemanları getirir  
print('Mor'in kume1)              #? kume1 de Sarı varsa TRUE yoksa FALSE döndürür     

print('Pembe' in kume1.union(kume2))   #? kume1 ve kume2 nin birleşiminde de Pembe varsa TRUE yoksa FALSE döndürür    




