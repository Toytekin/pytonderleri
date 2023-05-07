# sayi=input('Bir Sayi giriniz : ')
# intSayi=int(sayi)
# print('Sayinizin karesi')
# print(intSayi*intSayi)

# #! Girilen sayinmini faktöriyelini bulma

# faktoriyel=1

# gelenSayi=input('Bir sayi giriniz: ')
# intSayi=int(gelenSayi)

# for sayi in range(1,intSayi+1):
#     faktoriyel*=sayi
# print(f'{intSayi}! ={faktoriyel}')

#! Girilen sayinin asal olup olmadığını bulma



from pickle import FALSE


gelenSayi=input('Bir sayi giriniz: ')
intSayi=int(gelenSayi)
durum=False


for sayi in range(2, intSayi):
    if intSayi%sayi==0:
        durum=False
        break
    else:
        durum=True
        continue
if durum==True:
        print(f'{intSayi} bir asal sayidir')
else:
        print(f'{intSayi} bir asal sayı DEĞİLDİR')    
