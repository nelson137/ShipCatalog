import requests, re, platform
from collections import OrderedDict

def getShips(srcLoc, srcType='text'):
    if srcType == 'html':
        # get raw source code from website
        source = requests.get(srcLoc).content.decode()

        newlinePat = '\n'
        htmlPat = '<!DOCTYPE.+App.app = new |}\);.+<\/html>'
        inbetweenPat = '\[{"id":"\d+","slug"(.+?}){86}'
        source = re.sub(newlinePat, '', source)
        source = re.sub(htmlPat, '', source)
        source = re.sub(inbetweenPat, '', source)
    else:
        system = platform.system().lower()
        if system == "windows":
            path = "D:/Projects"
        elif system == "mac":
            path = "/Users/Nelson/Projects"
        elif system == "linux":
            path = "/home/nelson137/Projects"

        # get raw sourec code from file
        with open('{}/{}'.format(path, srcLoc), 'r') as f:
            source = f.read()

    # get ships stats from source code
    #allStatsPat = '{"id":"\d+","production_status":"[^{]+{[^[]+'
    allStatsPat = '{"id":"\d+","production_status":"[^{]+{([^,]+,){3}'
    allStats = re.findall(allStatsPat, source)

    ships = OrderedDict()

    # patterns for each stat
    modelPat = r'name":"([^"]+)","focus'
    mfrPat = r'name":"([^"]+)","known_for'
    focusPat = r'focus":"([^"]+)'
    prodstatPat = r'production_status":"([^"]+)'
    descPat = r'description":"([^"]+)","tagline'
    cargocapPat = r'cargocapacity":"([^"]+)'
    maxcrewPat = r'maxcrew":"([^"]+)'

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

    return ships