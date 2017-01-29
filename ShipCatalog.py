from GetShips import getShips
from SortShips import sortBy
from tClass import Ships
from random import shuffle

def main():
    '''(ships = getShips()
    
    maxcrews = shuffle(range(5))

    for shipN in ships.keys():
        ships[shipN]['max crew'] = maxcrews.pop()

    ships = sortBy('max crew')

    for ship in ships.values():
        print()
        print(ship)'''

    ships = Ships()

    print(ships.manufacturers)

if __name__ == "__main__":
    main()
