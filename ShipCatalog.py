from Ships import Ships
#from GetShips import getShips
#from SortShips import sortBy
#from random import shuffle

def main():
    ships = Ships()

    #ordered = list(ships.byModel.items())
    #ordered = list(ships.byManufacturer.items())
    #ordered = list(ships.byProductionStatus.items())
    #ordered = list(ships.byCargoCapacity.items())
    #ordered = list(ships.byMaxCrew.items())

    keys = ['manufacturer', 'model', 'production status']
    for key in keys:
        print(ships.getAllOfKey(key))

if __name__ == "__main__":
    main()