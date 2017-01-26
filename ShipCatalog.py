import re
from collections import OrderedDict
'''
KEY:
m = manufacturer
ps = production status
cc = cargo capacity
mc = max crew
'''



with open('{}/Git/ShipCatalog/5ShipsSource.txt'.format(path), 'r') as f:
    shipsDataSource = f.read()

allStatsPattern = '''{"id":"\d+","production_status":"[^{]+{[^[]+'''
allStatsMOS = re.findall(allStatsPattern, shipsDataSource)

ships = OrderedDict()

def SortByStat(stat, ship, lastShip=False):
    global used, byStat
    mKeys = ['Aegis Dynamics', 'Anvil Aerospace', 'ARGO ASTRONAUTICS', 'Banu', 'Consolidated Outland', 'Crusader Industries', 'Drake Interplanetary', 'Esperia', 'Kruger Intergalactic', 'Musashi Industrial &amp; Starflight Concern', 'Origin Jumpworks GmbH', 'Roberts Space Industries', 'Vanduul', "Xi'An"]
    psKeys = ['announced', 'in-concept', 'in-production', 'hangar-ready', 'flight-ready']
    for k in byStat[stat].keys(): byStat[stat][k].sort()
    byStat[stat] = sorted(byStat[stat].items(), key=lambda x: sortKeys[stat].index(x[0]))



modelPattern = r'''(name":")([^"]+)(","focus)'''
mPattern = r'''(name":")([^"]+)(","known_for)'''
focusPattern = r'''(focus":")([^"]+)'''
psPattern = r'''(production_status":")([^"]+)'''
descriptionPattern = r'''(description":")([^"]+)(","tagline)'''
ccPattern = r'''(cargocapacity":")([^"]+)'''
mcPattern = r'''(maxcrew":")([^"]+)'''

# funcs = [SortByModel, SortByM, SortByPs, SortByCc, SortByMc]
for statsIndex in range(len(allStatsMOS)):
    allStatsMOS[statsIndex] = re.sub(r'\\', '', allStatsMOS[statsIndex])

    model = re.search(modelPattern, allStatsMOS[statsIndex]).group(2)
    m = re.search(mPattern, allStatsMOS[statsIndex]).group(2)
    focus = re.search(focusPattern, allStatsMOS[statsIndex]).group(2)
    ps = re.search(psPattern, allStatsMOS[statsIndex]).group(2)
    description = re.search(descriptionPattern, allStatsMOS[statsIndex]).group(2)
    cc = re.search(ccPattern, allStatsMOS[statsIndex]).group(2)
    mc = re.search(mcPattern, allStatsMOS[statsIndex]).group(2)

    if statsIndex == len(allStatsMOS)-1: SortByStat(0, (m, model), lastShip=True)
    else: SortByStat(0, (m, model))

    if statsIndex == len(allStatsMOS)-1: SortByStat(0, (ps, model), lastShip=True)
    else: SortByStat(1, (ps, model))

    if statsIndex == len(allStatsMOS)-1: SortByStat(0, (cc, model), lastShip=True)
    else: SortByStat(2, (cc, model))

    if statsIndex == len(allStatsMOS)-1: SortByStat(0, (mc, model), lastShip=True)
    else: SortByStat(3, (mc, model))

    '''ships[model] = OrderedDict([('manufacturer', m),
                                ('productionstatus', ps),
                                ('focus', focus),
                                ('cargocapacity', cc),
                                ('maxcrew', mc),
                                ('description', description)])

    stats = [model, m, ps, cc, mc]
    for i in range(len(stats)):
        if statsIndex == len(allStatsMOS)-1:
            if i == 0: funcs[0](model, lastShip=True)
            else: funcs[i]((stats[i], model), lastShip=True)
        else:
            if i == 0: funcs[0](model)
            else: funcs[i]((stats[i], model))'''



#print(byMc)

print('-----END-----')
