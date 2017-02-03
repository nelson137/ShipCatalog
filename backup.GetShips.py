"""self.webSource = 'https://robertsspaceindustries.com/ship-specs'
    self.pWebSource = 'https://lethe.ca/phproxy/index.php?q=aHR0cHM6Ly9yb2JlcnRzc3BhY2VpbmR1c3RyaWVzLmNvbS9zaGlwLXNwZWNz'

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
    #source = str(requests.get(self.webSource).content).encode('utf-8').decode('utf-8')

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

    self.ships = ships
    self.byModel = OrderedDict(sorted(ships.items(), key=lambda item: item[1]['model']))
    self.byManufacturer = OrderedDict(sorted(ships.items(), key=lambda item: (item[1]['manufacturer'], item[1]['model'])))
    # byList #self.byProductionStatus = OrderedDict(sorted(ships.items(), key=lambda item: item[1]['production status']))
    self.byCargoCapacity = OrderedDict(sorted(ships.items(), key=lambda item: (item[1]['cargo capacity'], item[1]['model'])))
    self.byMaxCrew = OrderedDict(sorted(ships.items(), key=lambda item: (item[1]['max crew'], item[1]['model'])))"""