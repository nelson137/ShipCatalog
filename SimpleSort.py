from collections import OrderedDict

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

testing = [(0, [('Anvil Aerospace', 'w'), ("Xi'An", 'a'), ('Anvil Aerospace', 'b'), ('Crusader Industries', 'x'), ('Drake Interplanetary', 'a')]),
            (1, [('in-concept', 'd'), ('in-production', 'z'), ('announced', 'a'), ('flight-ready', 'b'), ('in-production', 'a')]),
            (2, [(99, 'c'), (0, 'z'), (0, '99'), (2, 'w'), (7, 'a')]),
            (3, [(4, 'z'), (0, 'a'), (5, 'w'), (0, 'b'), (4, 'a')])]
for statIandData in testing:
    for n in range(len(statIandData[1])):
        if n == len(statIandData[1])-1:
            SortByStat(statIandData[0], statIandData[1][n], lastShip=True)
        else:
            SortByStat(statIandData[0], statIandData[1][n])