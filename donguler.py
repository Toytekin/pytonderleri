
import math
# range(2,20,3)  ==> Burada döngü 2. indexden başlayarak 3 er 3 er ilerleyip 20. indexe kadar sürecek demek


# for i in range(0,10):  #?  range(0,10) 0 dan başlayarak 9 a kadar sayiları yazar 
#     print(i)

#! Örenewk 2 üzeri 10 hesaplama

# sonuc=1

# for i in range(10):
#     sonuc*=2
# print(sonuc)    


#! Örenek  ikim listeyi for döngüsüne sokmak

harfler=['a','b','c']
sayilar=[1,2,3]

# for harf in harfler:
#     if harf=='a':
#         for sayi in sayilar:
#              print(f'{harf} ve {sayi}')
#     elif harf=='b':
#          for sayi in sayilar:
#             print(f'{harf} ve {sayi*10}')
#     elif harf=='c':
#         for sayi in sayilar:
#             print(f'{harf} ve {sayi*100}')



sayilar2=[1,2,3,4,5,6,7]
# #! CONTİNUE  ile dögüyü sürdürebiliriz
# #  Mesela aşağıdaki örnekte sayilar listesinde 3 rakamını görünce yazdırmadan direk diğerlerini okutucaz
# #  Çıktı 1,2,4,5,6,7



# for sayi in sayilar2:
#       if sayi==3:
#         continue
#       else:
#         print(sayi)

# #! BREAK  ile dögüyü sonlandırırız
# #  Mesela aşağıdaki örnekte sayilar listesinde 3 rakamını görünce döngü sonlandırılacaktır
# #  Çıktı 1,2

# for sayi in sayilar2:
#       if sayi==3:
#         break
#       else:
#         print(sayi)
              

#  #! Örnek
#  # 100 kadar olan sayılardan 3 e bölünen sayıları yazdır             

# liste=range(100)  #? 100 kadar olanların listesini yaptık

# for sayi in liste:
#     if sayi%3==0:       # Burada mod ile 3 'e bölünebiliyorsa gibi bir sorgu yaptık    
#         print(sayi)
#     else:continue   


# #!  WHİLE
# # while şart sağlandığı sürece dögü devam eder

# sayi=2

# while sayi<10 :
#     sayi+=1 
#     print(sayi)


#! Örenek 1 den 100 e kadar olan sayılarda süper pisagoru bulma

sayiList1=range(100)
sayiList2=range(100)
def is_perfect_square(n):
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n


for sayi1 in sayiList1:
    for sayi2 in sayilar2:
        if (is_perfect_square((sayi1*sayi1)+(sayi2*sayi2))):
                print((sayi1*sayi1)+(sayi2*sayi2))
        else:
                continue




