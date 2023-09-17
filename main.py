slownik = {
    'Mama': 46545646456,
    'Alex': 1231236,
    'Mateusz': 13436456,
    'Michal': 463453456456,
}


name = input('Podaj kontakt')
if name in slownik.keys():
    print(name, ':', slownik[name])
else:
    print('niema takiego kontaktu')
