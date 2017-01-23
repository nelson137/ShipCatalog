from collections import OrderedDict

used = [[], [], [], []] # [usedManufacturers, usedProductionstats, usedCapacities, usedMaxcrews]
byStat = [OrderedDict(), OrderedDict(), OrderedDict(), OrderedDict()] # [byManufacturer, byProductionstat, byCargocapacity, byMaxcrew]
def SortStats(shipData):
    '''Sort Ship Data into OrderedDicts'''
    global used, byStat

    m = (shipData[0], shipData[-1])
    ps = (shipData[1], shipData[-1])
    cc = (shipData[2], shipData[-1])
    mc = (shipData[3], shipData[-1])

    for n in range(len(shipData)-1):
        print(n)

SortStats(['Esperia', 'announced', 12, 2, 'Mustang'])