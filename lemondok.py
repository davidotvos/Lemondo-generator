import datetime


honapok = {
    '01' : 'január',
    '02' : 'február',
    '03' : 'március',
    '04' : 'április',
    '05' : 'május',
    '06' : 'június',
    '07' : 'július',
    '08' : 'augusztus',
    '09' : 'szeptember',
    '10' : 'október',
    '11' : 'november',
    '12' : 'december'
}

varos = 'Debrecen'
_felelos = 'Alföldi Imre'


def getdatum():
    d = str(datetime.date.today()).split('-')
    d[1] = honapok.get(d[1])(d[1])
    result = '. '.join(d[:2]) + ' ' + d[2] + '.'

    return result


class Lemondo:
    def __init__(self, tervcim, iktatoszam, tipus, dátum, felelos):
        self.tervcim = tervcim
        self.iktatoszam = iktatoszam
        self.tipus = tipus
        self.dátum = getdatum()
        self.felelos = _felelos

    def __str__(self):
        return f'tervcím: {self.tervcim}, iktatószám: {self.iktatoszam}, típus: {self.tipus}'