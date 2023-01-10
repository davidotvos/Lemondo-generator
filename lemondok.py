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

varos = "Debrecen"


def getdatum(honap_szam):
    """

    """

    d = str(datetime.date.today()).split('-')
    d[1] = honapok.get(honap_szam)(d[1])
    result = '. '.join(d[:2]) + ' ' + d[2] + '.'

    return result


class Lemondo:
    def __init__(self, tervcim, iktatoszam, tipus, dátum):
        pass