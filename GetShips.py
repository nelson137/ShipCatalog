import re, platform
from collections import OrderedDict

def getShips():
    system = platform.system().lower()
    if system == "windows":
        path = "D:/Projects"
    elif system == "mac":
        path = "/Users/Nelson"
    elif system == "linux":
        path = "/home/nelson137"

    with open('{}/Git/ShipCatalog/sources/5ships.txt'.format(path), 'r') as f:
        shipsDataSource = f.read()

    allStatsPattern = '''{"id":"\d+","production_status":"[^{]+{[^[]+'''
    allStatsMOS = re.findall(allStatsPattern, shipsDataSource)

    ships = OrderedDict()

    modelPat = r'''name":"([^"]+)","focus'''
    mfrPat = r'''name":"([^"]+)","known_for'''
    focusPat = r'''focus":"([^"]+)'''
    prodstatPat = r'''production_status":"([^"]+)'''
    descPat = r'''description":"([^"]+)","tagline'''
    cargocapPat = r'''cargocapacity":"([^"]+)'''
    maxcrewPat = r'''maxcrew":"([^"]+)'''

    for statsIndex in range(len(allStatsMOS)):
        allStatsMOS[statsIndex] = re.sub(r'\\', '', allStatsMOS[statsIndex])

        model = re.search(modelPat, allStatsMOS[statsIndex]).group(1)
        mfr = re.search(mfrPat, allStatsMOS[statsIndex]).group(1)
        focus = re.search(focusPat, allStatsMOS[statsIndex]).group(1)
        prodstat = re.search(prodstatPat, allStatsMOS[statsIndex]).group(1)
        desc = re.search(descPat, allStatsMOS[statsIndex]).group(1)
        cargocap = re.search(cargocapPat, allStatsMOS[statsIndex]).group(1)
        maxcrew = re.search(maxcrewPat, allStatsMOS[statsIndex]).group(1)

        ships[model] = OrderedDict([('model', model),
                                    ('manufacturer', mfr),
                                    ('focus', focus),
                                    ('production status', prodstat),
                                    ('description', desc),
                                    ('cargo capacity', cargocap),
                                    ('max crew', maxcrew)])

    return ships
