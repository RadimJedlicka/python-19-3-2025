import os
from random import choice, seed

from slova import hadana_slova
from grafika import obesenec


def hangman():
    zivoty = 7
    hra_bezi = True
    hra(zivoty, hra_bezi)
def hra(zivoty, hra_bezi):
    seed(2) # slovo je 'vojna'
    slovo = choice(hadana_slova)
    tajenka = vytvor_tajenku(slovo, "_")
    while hra_bezi and zivoty:
        zobraz_stav_hry(tajenka, zivoty)

        hadani = input('Hadej pismeno/cele slovo: ')

        if hadani == slovo:
            hra_bezi = False
        elif hadani in slovo and len(hadani) == 1:
            indexy = je_pismeno_ve_slove(slovo, hadani)
            if indexy:
                tajenka = prepis_pismeno(indexy, tajenka, hadani)
            hra_bezi = kompletni_tajenka(tajenka)
        else:
            print('Pismeno neni v tajence, hadej znova!')
            zivoty -= 1
    else:
        konec_hry(hra_bezi, slovo)
def konec_hry(hra_bezi, slovo):
    if hra_bezi == False:
        print('Vyhral jsi!')
    else:
        print(f'Prohral jsi, tajenka byla "{slovo}"')
def kompletni_tajenka(tajenka):
    return False if '_' not in tajenka else True
def prepis_pismeno(indexy, tajenka, hadani):
    for index in indexy:
        tajenka[index] = hadani
    return tajenka
def je_pismeno_ve_slove(slovo, hadani):
    return [
        index for index, symbol in enumerate(slovo) 
        if hadani in symbol
        ]

def zobraz_stav_hry(tajenka, zivoty):
    os.system('cls')
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(f"Zbyvajici pocet zivotu: {zivoty}")
def vytvor_tajenku(slovo, znak):
    return len(slovo) * [znak]
hangman()