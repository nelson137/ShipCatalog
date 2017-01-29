import platform, requests, re
from collections import OrderedDict

class Ships:
    def __init__(self):
    	# use self.webSource to download ships-specs source code
        self.webSource = 'https://robertsspaceindustries.com/ship-specs'

        system = platform.system().lower()
        if system == "windows":
            path = "D:/Projects"
        elif system == "mac":
            path = "/Users/Nelson"
        elif system == "linux":
            path = "/home/nelson137"

        # get code data from file
        with open('{}/Git/ShipCatalog/sources/5ships.txt'.format(path), 'r') as f:
            source = f.read()

        # get source code from website
        source = str(requests.get(self.webSource).content).encode('utf-8').decode('utf-8')
        print(source[:6000])

        # get ships stats from source code
        allStatsPat = '''{"id":"\d+","production_status":"[^{]+{[^[]+'''
        allStats = re.findall(allStatsPat, source)

        ships = OrderedDict()

        # patterns for each stat
        modelPat = r'''name":"([^"]+)","focus'''
        mfrPat = r'''name":"([^"]+)","known_for'''
        focusPat = r'''focus":"([^"]+)'''
        prodstatPat = r'''production_status":"([^"]+)'''
        descPat = r'''description":"([^"]+)","tagline'''
        cargocapPat = r'''cargocapacity":"([^"]+)'''
        maxcrewPat = r'''maxcrew":"([^"]+)'''

        for index in range(len(allStats)):
            allStats[index] = re.sub(r'\\', '', allStats[index])

            # get stat from source code of each ship
            model = re.search(modelPat, allStats[index]).group(1)
            mfr = re.search(mfrPat, allStats[index]).group(1)
            focus = re.search(focusPat, allStats[index]).group(1)
            prodstat = re.search(prodstatPat, allStats[index]).group(1)
            desc = re.search(descPat, allStats[index]).group(1)
            cargocap = re.search(cargocapPat, allStats[index]).group(1)
            maxcrew = re.search(maxcrewPat, allStats[index]).group(1)

            # put stats into OrderedDict
            ships[model] = OrderedDict([('model', model),
            							('manufacturer', mfr),
            							('focus', focus),
            							('production status', prodstat),
            							('description', desc),
            							('cargo capacity', cargocap),
            							('max crew', maxcrew)])

        # compile list of all manufacturers
        manufacturers = []
        for ship in ships.values():
        	manufacturers.append(ship['manufacturer'])
        manufacturers = list(set(manufacturers))

        self.ships = ships
        self.manufacturers = manufacturers

    def sortBy(self, key):
        def byABC(key):
            pass

        def byList(key, lst):
            pass

        if key == 'model':
            byABC(key)
        elif key == 'manufacturer':
            byList(key, [])
        elif key == 'production status':
            byList(key, [])
        elif key == 'cargo capacity':
            byList(key, [])
        elif key == 'max crew':
            byList(key, [])