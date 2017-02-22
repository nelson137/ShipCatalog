from os.path import dirname, abspath 
from collections import OrderedDict
from GetShips import getShips

class Catalog:
    '''Catalog object class'''
    def __init__(self):
        #self.ships = getShips('https://robertsspaceindustries.com/ship-specs', 'html')
        parentDir = dirname(abspath(__file__))
        print(parentDir)
        ships = getShips('%s/sources/all-ships.txt' % parentDir)
        prodstats = ['flight-ready', 'hangar-ready', 'ready', 'in-production', 'in-concept', 'announced']

        byModel = OrderedDict(sorted(ships.items(), key=lambda item: item[1]['model']))
        byManufacturer = OrderedDict(sorted(ships.items(), key=lambda item: (item[1]['manufacturer'], item[1]['model'])))
        byProductionStatus = OrderedDict(sorted(ships.items(), key=lambda item: (prodstats.index(item[1]['production status']), item[1]['model'])))
        byCargoCapacity = OrderedDict(sorted(ships.items(), key=lambda item: (item[1]['cargo capacity'], item[1]['model'])))
        byMaxCrew = OrderedDict(sorted(ships.items(), key=lambda item: (item[1]['max crew'], item[1]['model'])))

        self.allOrders = {
            'ships' : ships,
            'model' : byModel,
            'manufacturer' : byManufacturer,
            'production status' : byProductionStatus,
            'cargo capacity' : byCargoCapacity,
            'max crew' : byMaxCrew
        }

    def getAllOf(self, key, order='ships', unique=False):
        all_ = []
        for ship in self.allOrders[order].values():
            all_.append(ship[key])

        return all_ if not unique else list(set(all_))
