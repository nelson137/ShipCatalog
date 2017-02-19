from collections import OrderedDict
from GetShips import getShips

class Ships:
    '''Ships object'''
    def __init__(self):
        #self.ships = getShips('https://robertsspaceindustries.com/ship-specs', 'html')
        self.ships = getShips('Git/ship-catalog/sources/all-ships.txt')
        self.numShips = len(self.ships.items())

        self.byModel = OrderedDict(sorted(self.ships.items(), key=lambda item: item[1]['model']))
        self.byManufacturer = OrderedDict(sorted(self.ships.items(), key=lambda item: (item[1]['manufacturer'], item[1]['model'])))
        self.byProductionStatus = OrderedDict(sorted(self.ships.items(), key=lambda item: (['flight-ready', 'hangar-ready', 'ready', 'in-production', 'in-concept', 'announced'].index(item[1]['production status']), item[1]['model'])))
        self.byCargoCapacity = OrderedDict(sorted(self.ships.items(), key=lambda item: (item[1]['cargo capacity'], item[1]['model'])))
        self.byMaxCrew = OrderedDict(sorted(self.ships.items(), key=lambda item: (item[1]['max crew'], item[1]['model'])))

    def getAllOf(self, key, order='ships', unique=False):
        allOrders = {
            'ships' : self.ships,
            'model' : self.byModel,
            'manufacturer' : self.byManufacturer,
            'production status' : self.byProductionStatus,
            'cargo capacity' : self.byCargoCapacity,
            'max crew' : self.byMaxCrew
        }
        all_ = []
        for ship in allOrders[order].values():
            all_.append(ship[key])

        return all_ if not unique else list(set(all_))
