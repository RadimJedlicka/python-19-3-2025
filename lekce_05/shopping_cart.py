# TODO promenne
sklad = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""

oddelovac = '=' * 40

# ----------------------------

# TODO kosik
kosik = {}

# TODO Pozdrav a vypsani nabidky
print(
    "Vitejte u naseho nakupniho kosiku!".center(len(oddelovac)),
    oddelovac,
    nabidka,
    sep="\n"
)

# TODO cely cyklus
while (zbozi := input("Zadejte zbozi: ")) != "konec":
    #continue

    # TODO pokud zbozi nebude na sklade
    if zbozi not in sklad:
        print(f"Zbozi {zbozi} neni na sklade.")
        continue

    # TODO Pokud vybrane zbozi neni v nakupnim kosiku
    elif zbozi not in kosik and sklad[zbozi][1] > 0:
        # TODO pridame zbozi do kosiku:
        kosik[zbozi] = [sklad[zbozi][0], 1]  # cena, mnozstvi

        # TODO odecteme zbozi ze skladu
        sklad[zbozi][1] = sklad[zbozi][1] - 1

    # TODO pokud zbozi je v kosiku
    elif zbozi in kosik and sklad[zbozi][1] > 0:
        kosik[zbozi][1] +=  1
        sklad[zbozi][1] -=  1

    # TODO pokud zbozi jiz neni skladem
    elif sklad[zbozi][1] == 0:
        print(f"Zbozi {zbozi} neni na sklade.")
        continue

# TODO vypis kosiku
else:
    print(f'kosik je: {kosik}')
    print(f'sklad je: {sklad}')


suma = []
for polozka in kosik:
    suma.append(kosik[polozka][0] * kosik[polozka][1])

celkem = sum(suma)
print(f"Celkem: {celkem}")