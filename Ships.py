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

    def getAllOfKey(self, key):
        '''returns unique list of all of key in Ships'''
        all_ = []
        for ship in self.ships.values():
        	all_.append(ship[key])

        return list(set(all_))
