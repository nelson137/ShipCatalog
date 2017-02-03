from collections import OrderedDict
from GetShips import getShips

class Ships:
    def __init__(self):
        self.ships = getShips('Git/ShipCatalog/sources/5ships.txt')
        self.byModel = OrderedDict(sorted(self.ships.items(),
                                          key=lambda item: item[1]['model']))
        self.byManufacturer = OrderedDict(sorted(self.ships.items(),
                                                 key=lambda item: (item[1]['manufacturer'], item[1]['model'])))
        self.byProductionStatus = OrderedDict(sorted(self.ships.items(),
                                                     key=lambda item: item[1]['production status'])) # sort by custom list
        self.byCargoCapacity = OrderedDict(sorted(self.ships.items(),
                                                  key=lambda item: (item[1]['cargo capacity'], item[1]['model'])))
        self.byMaxCrew = OrderedDict(sorted(self.ships.items(),
                                            key=lambda item: (item[1]['max crew'], item[1]['model'])))

    def getMfrs(self):
        '''compile list of all manufacturers'''

        manufacturers = []
        for ship in self.ships.values():
        	manufacturers.append(ship['manufacturer'])

        return list(set(manufacturers))