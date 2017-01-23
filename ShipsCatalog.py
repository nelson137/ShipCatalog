import re
from collections import OrderedDict
'''
KEY:
m = manufacturer
ps = production status
cc = cargo capacity
mc = max crew
'''


print('-----START-----')

with open('D:\Projects\Python\Star Citizen\Ships Catalog\\5shipsSourceCode.txt', 'r') as f:
    shipsDataSource = f.read()

allStatsPattern = '''{"id":"\d+","production_status":"[^{]+{[^[]+'''
allStatsMOS = re.findall(allStatsPattern, shipsDataSource)

ships = OrderedDict()

allModels = []
byModel = OrderedDict()
def SortByModel(ship, lastShip=False):
    global allModels

    allModels.append(ship)

    if lastShip == True:
        allModels.sort()
        for ship in allModels:
            byModel[ship] = ships[ship]

used = [[], [], [], []] # [usedManufacturers, usedProductionstats, usedCapacities, usedMaxcrews]
byStat = [OrderedDict(), OrderedDict(), OrderedDict(), OrderedDict()] # [byManufacturer, byProductionstat, byCargocapacity, byMaxcrew]
def SortByStat(stat, ship, lastShip=False):
    '''stat:
    0 = manufacturer
    1 = production status
    2 = cargo capacity
    3 = max crew
    '''
    global used, byStat

    if ship[0] not in used[stat]:
        used[stat].append(ship[0])
        byStat[stat][ship[0]] = [ship[1]]
    else: byStat[stat][ship[0]].append(ship[1])

    if lastShip == True:
        if stat == 0:
            mKeys = ['Aegis Dynamics', 'Anvil Aerospace', 'ARGO ASTRONAUTICS', 'Banu', 'Consolidated Outland', 'Crusader Industries', 'Drake Interplanetary', 'Esperia', 'Kruger Intergalactic', 'Musashi Industrial &amp; Starflight Concern', 'Origin Jumpworks GmbH', 'Roberts Space Industries', 'Vanduul', "Xi'An"]
        else:
             mKeys = []
        if stat == 1:
            psKeys = ['announced', 'in-concept', 'in-production', 'hangar-ready', 'flight-ready']
        else:
            psKeys = []
        if stat == 2:
            used[2].sort()
            ccKeys = range(used[2][-1]+1)
        else:
            ccKeys = []
        if stat == 3:
            used[3].sort()
            mcKeys = range(used[3][-1]+1)
        else:
            mcKeys = []
        sortKeys = [mKeys, psKeys, ccKeys, mcKeys]

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