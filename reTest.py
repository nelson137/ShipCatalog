import re, platform
from collections import OrderedDict

system = platform.system().lower()
if system == "windows":
    path = "D:/Projects"
elif system == "mac":
    path = "/Users/Nelson"
elif system == "linux":
    path = "/home/nelson137"

with open('{}/Git/ShipCatalog/5ShipsSource.txt'.format(path), 'r') as f:
    shipsDataSource = f.read()

allStatsPattern = '''{"id":"\d+","production_status":"[^{]+{[^[]+'''
allStatsMOS = re.findall(allStatsPattern, shipsDataSource)

ships = OrderedDict()

modelPattern = r'''name":"([^"]+)","focus'''
mPattern = r'''name":"([^"]+)","known_for'''
focusPattern = r'''focus":"([^"]+)'''
psPattern = r'''production_status":"([^"]+)'''
descriptionPattern = r'''description":"([^"]+)","tagline'''
ccPattern = r'''cargocapacity":"([^"]+)'''
mcPattern = r'''maxcrew":"([^"]+)'''

for statsIndex in range(len(allStatsMOS)):
    allStatsMOS[statsIndex] = re.sub(r'\\', '', allStatsMOS[statsIndex])

    model = re.search(modelPattern, allStatsMOS[statsIndex]).group(1)
    mfr = re.search(mPattern, allStatsMOS[statsIndex]).group(1)
    focus = re.search(focusPattern, allStatsMOS[statsIndex]).group(1)
    prodstat = re.search(psPattern, allStatsMOS[statsIndex]).group(1)
    desc = re.search(descriptionPattern, allStatsMOS[statsIndex]).group(1)
    cargocap = re.search(ccPattern, allStatsMOS[statsIndex]).group(1)
    maxcrew = re.search(mcPattern, allStatsMOS[statsIndex]).group(1)

    ships[model] = OrderedDict([('model', model), ('manufacturer', mfr), ('focus', focus), ('production status', prodstat), ('description', desc), ('cargo capacity', cargocap), ('max crew', maxcrew)])

print(ships.values())
