import os
from random import choice

def vyber_tajne_slovo(list_hadanych_slov):
    slovo = choice(list_hadanych_slov)
    return slovo

def vytvor_tajenku(slovo):
    tajenka = ['_'] * len(slovo)
    return tajenka

def zobraz_stav_hry(tajenka, zivoty):
    os.system("cls") # clear
    joined_tajenka = ' '.join(tajenka)
    print(joined_tajenka)
    print(f"Zbyvajici pocet zivotu: {zivoty}")

def hlavni_hra():
    hadana_slova = ['dva', 'hudba', 'vecernicek']
    zivoty = 7
    hra_bezi = True

    tajne_slovo = vyber_tajne_slovo(hadana_slova)
    tajenka_list = vytvor_tajenku(tajne_slovo)

    while hra_bezi and zivoty > 0:
        zobraz_stav_hry(tajenka_list, zivoty)
        break

if __name__ == "__main__": 
    hlavni_hra()