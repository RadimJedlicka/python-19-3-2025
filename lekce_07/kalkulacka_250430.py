import math

def zobraz_nabidku(args):
    spojeni = ' | '.join(args)
    oddelovac = '-' * len(spojeni)
    print(oddelovac, spojeni, oddelovac, sep='\n')

# TODO umocnovani
def umocnovani():
    mocnenec = float(input('Zadejte mocnenec: '))
    mocnitel = float(input('Zadejte mocnitel: '))

    vysledek = mocnenec ** mocnitel
    print(f'Vysledek: {vysledek}')


# TODO aritmeticky prumer
def aritmeticky_prumer():
    list_cisel = []
    while (cislo := input('Zadej cislo: ')) != '=':
        if cislo.isnumeric():
            list_cisel.append(float(cislo))
        else:
            print('Zadej cislo!')

    vysledek = sum(list_cisel) / len(list_cisel)
    print(f'Vysledek: {vysledek}')


def kalkulacka():
    # TODO smycka while
    while True:
        
        # TODO zobrazit nabidku
        nabidka = ('+', '-', '*', '/', 'avg', 'pow', 'sin', 'quit')
        zobraz_nabidku(nabidka)

        # TODO ziskat vstup od uzivatele
        vyber = input('Zadejte operaci: ')

        if vyber == 'quit':
            print('Konec programu')
            break

        elif vyber == 'pow':
            umocnovani()

        elif vyber == 'avg':
            aritmeticky_prumer()

        elif vyber == 'sin':
            vypocti_sinus()

        elif vyber in ('+', '-', '*', '/'):
            zakladni_arit_op()



def zakladni_arit_op():
    zapis = input('Zadejte zapis: ')
    vysledek = eval(zapis)

    print(f'Vysledek: {vysledek}')



def vypocti_sinus():
    uhel = float(input('Zadejte uhel v radianech: '))
    vysledek = math.sin(uhel)
    print(f'Vysledek: {vysledek}')

if __name__ == '__main__':
    kalkulacka()







