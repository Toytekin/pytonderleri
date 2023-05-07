
#! 1
#   10'un altındaki 3 veya 5'in katı olan tüm doğal sayıları sıralarsak
#   3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür.
#   1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.

gelenSayilar=[]


for sayi in range(1,1000):
    if sayi%3==0 or sayi%5==0:
        gelenSayilar.append(sayi)

toplam=sum(gelenSayilar)
print(toplam)   


#! 2
# Fibonacci dizisindeki her yeni terim, önceki iki terimin eklenmesiyle oluşturulur.
#  1 ve 2 ile başlayarak ilk 10 terim şöyle olacaktır:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Değerleri dört milyonu geçmeyen Fibonacci dizisindeki terimleri dikkate alarak çift 
# değerli terimlerin toplamını bulunuz.

def fibonacci(n):
    # Fibonacci dizisindeki n. terimi hesaplayan fonksiyon
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

total = 0
n = 1
while fibonacci(n) <= 10:
    if fibonacci(n) % 2 == 0:
        total += fibonacci(n)
    n += 1

print(total)