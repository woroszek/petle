a = int(input('Ile paczek pragniesz wysłać? '))
waga_ogolna = 0
waga_paczki = 0
licznik_paczek = 0
taba= []

for i in range(a):
    waga_ost_elem = float(input(f'Jaka jest waga paczki nr. {i+1}? '))
    if waga_ost_elem > 10 or waga_ost_elem < 1:
        if waga_paczki > 0:
            licznik_paczek += 1
            taba.append(20 - waga_paczki)
            break
        else:
            waga_ogolna += waga_ost_elem
            break
    waga_ogolna += waga_ost_elem
    if waga_paczki + waga_ost_elem > 20:
        licznik_paczek += 1
        taba.append(20 - waga_paczki)
        waga_paczki = 0 + waga_ost_elem
    else:
        waga_paczki += waga_ost_elem
    if i+1 == a:
        licznik_paczek += 1
        taba.append(20 - waga_paczki)
    
waga_pusta = licznik_paczek * 20 - waga_ogolna

if licznik_paczek > 1:
    print(f'Wysłano {licznik_paczek} paczki o łącznej masie {waga_ogolna} kg.')
    
elif licznik_paczek == 1:
    print(f'Wysłano {licznik_paczek} paczkę o łącznej masie {waga_ogolna} kg.')
    
else:
    print("Nie wysłano żadnej paczki.")
    
if waga_pusta > 0:
    print(f'Ogólna liczba pustych kilogramów w wysłanych paczkach to: {waga_pusta} kg.')
    print(f'Najwięcej pustych kilogramów miała paczka nr. {(taba.index(max(taba))+1)}: {max(taba)} pustych kilogramów.')
else:
    print("Brak pustych kilogramów")