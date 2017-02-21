from collections import OrderedDict
from GetShips import getShips

class Catalog:
    """Catalog object class"""
    def __init__(self):
        #self.ships = getShips('https://robertsspaceindustries.com/ship-specs', 'html')
        self.ships = getShips('Git/ship-catalog/sources/all-ships.txt')
        self.numShips = len(self.ships.items())
        self.prodstats = ['flight-ready', 'hangar-ready', 'ready', 'in-production', 'in-concept', 'announced']

        self.byModel = OrderedDict(sorted(self.ships.items(), key=lambda item: item[1]['model']))
        self.byManufacturer = OrderedDict(sorted(self.ships.items(), key=lambda item: (item[1]['manufacturer'], item[1]['model'])))
        self.byProductionStatus = OrderedDict(sorted(self.ships.items(), key=lambda item: (self.prodstats.index(item[1]['production status']), item[1]['model'])))
        self.byCargoCapacity = OrderedDict(sorted(self.ships.items(), key=lambda item: (item[1]['cargo capacity'], item[1]['model'])))
        self.byMaxCrew = OrderedDict(sorted(self.ships.items(), key=lambda item: (item[1]['max crew'], item[1]['model'])))

        self.allOrders = {
            'ships' : self.ships,
            'model' : self.byModel,
            'manufacturer' : self.byManufacturer,
            'production status' : self.byProductionStatus,
            'cargo capacity' : self.byCargoCapacity,
            'max crew' : self.byMaxCrew
        }

    def getAllOf(self, key, order='ships', unique=False):
        all_ = []
        for ship in self.allOrders[order].values():
            all_.append(ship[key])

        return all_ if not unique else list(set(all_))
