import random



#! notlar

#       and aslında && ile aynı  (ve)
#       or  aslında || ile aynu (veya)
#       elif aslında else if ile aynı anlamdadır
#       in ifadesi bir listede eleman varmı yokmu sorgulamnasını byaptığkjmz alan

a=random.randint(1, 104)
b=random.randint(1, 510)
c=random.randint(1, 140)


if a>=b and a>=c:
    if b>=c:
        print(f'{a} > {b} > {c}')
    else:
        print(f'{a} > {c} > {b}')
elif b>=a and b>=c:
    if a>=c:
        print(f'{b} > {a} > {c}')
    else:
        print(f'{b} > {c} > {a}')
elif c>=a and c>=b:
    if a>=b:
        print(f'{c} > {a} > {b}')
    else:
        print(f'{c} > {b} > {a}')
else:
    print('Beklenmedik bir hata oluştu')

sayilar=[1,2,5,6,687,23,6,5,4,]
aranacakSayi=95

if aranacakSayi in sayilar:
        print('Sayi var')
else:
        print('Sayi YOK ')
